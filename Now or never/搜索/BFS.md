# BFS
广度优先搜索一层一层地进行遍历，每层遍历都以上一层遍历的结果作为起点，遍历一个距离能访问到的所有节点。需要注意的是，遍历过的节点不能再次被遍历。

每一层遍历的节点都与根节点距离相同。设 di 表示第 i 个节点与根节点的距离，推导出一个结论：对于先遍历的节点 i 与后遍历的节点 j，有 di <= dj。利用这个结论，可以求解最短路径等 最优解 问题：第一次遍历到目的节点，其所经过的路径为最短路径。

在程序实现 BFS 时需要考虑以下问题：

    队列：用来存储每一轮遍历得到的节点；
    标记：对于遍历过的节点，应该将它标记，防止重复遍历。
	使用 BFS 只能求解无权图的最短路径，无权图是指从一个节点到另一个节点的代价都记为 1。




# [1091. 二进制矩阵中的最短路径](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/ "1091. 二进制矩阵中的最短路径")
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。

说明:

    如果不存在这样的转换序列，返回 0。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        # 题意是正方形
        length = len(grid)
        # 可以达到的每一个点可以到达的路径数组
        next = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        from collections import deque
        q = deque()
        # 前面两个是下标 后面是到达此点的步数
        q.append([0,0,1])
        while q:
            r , c , s = q.popleft()
            if r == length - 1 and c == length - 1:
                return s
            for i ,j  in next:
                next_r = i + r
                next_c = j + c
                if length>next_r>=0 and length>next_c>=0 and grid[next_r][next_c]==0:
                    q.append([next_r,next_c,s+1])
                    # 要去掉已经访问过的节点
                    grid[next_r][next_c] = 1
        return -1
```

# [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder/ "127. 单词接龙")
```python
from collections import defaultdict,deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        # 题意所有单词一个长度
        L = len(beginWord)
        all_words = defaultdict(list)
        for i in range(L):
            for word in wordList:
                # 生成字典里所有的转换序列后的词对应转换前的
                # 不同的单词可能变换后相同所以对应的value是一个变换前的列表
                all_words[ word[:i]+"*"+word[i+1:] ].append(word)
        q = deque()
        q.append( (beginWord, 1) )
        # 使用字典查找是否存在速度更快
        visited = {beginWord:1}
        while q:
            cur_word, res = q.popleft()
            for i in range(L):
                # 因为是defaultdict如果没有该单词就为空
                cur = cur_word[:i]+"*"+cur_word[i+1:]
                for j in all_words[cur]:
                    if j == endWord:
                        return res+1
                    if j not in visited:
                        visited[j] = 1
                        q.append( (j,res+1) )
        return 0
```