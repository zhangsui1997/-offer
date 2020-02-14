Backtracking（回溯）属于 DFS。

    普通 DFS 主要用在 可达性问题 ，这种问题只需要执行到特点的位置然后返回即可。
    而 Backtracking 主要用于求解 排列组合 问题，例如有 { 'a','b','c' } 三个字符，求解所有由这三个字符排列得到的字符串，这种问题在执行到特定的位置返回之后还会继续执行求解过程。

因为 Backtracking 不是立即返回，而要继续求解，因此在程序实现时，需要注意对元素的标记问题：

## 回溯过程中一定要注意已用过点的状态 如果当前回溯已经改变了他的状态但是不能返回正确结果一定要将其改回去 不然其他回溯要用它时 如果是已使用状态的话会返回错误结果如79. 单词搜索
    在访问一个新元素进入新的递归调用时，需要将新元素标记为已经访问，这样才能在继续递归调用时不用重复访问该元素；
    但是在递归返回时，需要将元素标记为未访问，因为只需要保证在一个递归链中不同时访问一个元素，可以访问已经访问过但是不在当前递归链中的元素。
## 对于全排列的问题 backtracking函数参数一般是(已经排列的结果，剩下的元素) 如果是坐标问题就是(传当前坐标，使用过的坐标，当前结果)这个模板
# [257. 二叉树的所有路径](https://leetcode-cn.com/problems/binary-tree-paths/ "257. 二叉树的所有路径")
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

输入:

   1
 /   \
2      3
 \
  5
输出: ["1->2->5", "1->3"]
```python
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def construct_paths(root, path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:  # 当前节点是叶子节点
                    paths.append(path)  # 把路径加入到答案中
                else:
                    path += '->'  # 当前节点不是叶子节点，继续递归遍历
                    construct_paths(root.left, path)
                    construct_paths(root.right, path)

        paths = []
        construct_paths(root, '')
        return paths
```
# [46. 全排列](https://leetcode-cn.com/problems/permutations/ "46. 全排列")
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        r = []
        # 已经形成的 和 剩下的
        def backtracking(res, others):
            if len(res) == n:
                r.append(res)
                return
            else:
                for i in range(len(others)):
                    backtracking(res+[others[i]], others[:i]+others[i+1:])

        backtracking([],nums)
        return r
```
# [79. 单词搜索](https://leetcode-cn.com/problems/word-search/ "79. 单词搜索")
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        to = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # 行数 列数
        row, col = len(board), len(board[0])
        # 单词长度
        n = len(word)

        # index是单词下标
        def backtracking(index, r, c,used):
            if index == n and 0 <= r < row and 0 <= c < col:
                return True
            else:
                for t in to:
                    new_r = r + t[0]
                    new_c = c + t[1]
                    if 0 <= new_r < row and 0 <= new_c < col and (new_r, new_c) not in used:
                        if board[new_r][new_c] == word[index]:
                            used.add((new_r, new_c))
                            if backtracking(index + 1, new_r, new_c,used):
                                return True
                            else:
                                continue
                # 当该点返回false时要将它从used中删除 因为可能会有其他回溯用到
                used.remove((r,c))
                return False
        for r in range(row):
            for c in range(col):
                # 找到符合word第一个字母的才开始回溯
                if board[r][c] == word[0]:
                    # 构建一个hashset保存用过的字母下标
                    used = set()
                    used.add((r, c))
                    if backtracking(1, r, c, used):
                        return True
        return False
```

# [93. 复原IP地址](https://leetcode-cn.com/problems/restore-ip-addresses/ "93. 复原IP地址")
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 我们要知道IP的格式,每位是在0~255之间
        res = []
        n = len(s)
        # index 当前到了哪一位
        # string 当前形成的答案
        # flag 剩下的部分 ip地址只有4部分如255.255.255.1
        def backtrack(index, string, flag):
            if index == n and flag == 0:
                # 为了处理"."要去掉最后一位
                res.append(string[:-1])
                return
            if flag < 0:
                return
            # 一个部分最多只有三位数
            for i in range(index,index+3):
            # 不能出现以0开头的两位以上数字,比如012,08
                if i < n:
                    if i == index and s[i] == "0":
                        backtrack(i + 1, string + s[i] + ".", flag-1)
                        # 遇到0推出该flag部分的循环 避免出先012,08等情况
                        break
                    elif 0 < int(s[index : i+1]) <= 255:
                        backtrack(i + 1, string + s[index:i+1] + ".", flag-1)
        backtrack(0, "", 4)
        return res
```
