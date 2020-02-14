广度优先搜索一层一层遍历，每一层得到的所有新节点，要用队列存储起来以备下一层遍历的时候再遍历。

而深度优先搜索在得到一个新节点时立即对新节点进行遍历：从节点 0 出发开始遍历，得到到新节点 6 时，立马对新节点 6 进行遍历，得到新节点 4；如此反复以这种方式遍历新节点，直到没有新节点了，此时返回。返回到根节点 0 的情况是，继续对根节点 0 进行遍历，得到新节点 2，然后继续以上步骤。

从一个节点出发，使用 DFS 对一个图进行遍历时，能够遍历到的节点都是从初始节点可达的，DFS 常用来求解这种 可达性 问题。

在程序实现 DFS 时需要考虑以下问题：

    栈：用栈来保存当前节点信息，当遍历新节点返回时能够继续遍历当前节点。可以使用递归栈。
    标记：和 BFS 一样同样需要对已经遍历过的节点进行标记。

# [130. 被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/ "130. 被围绕的区域")
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)

        # 如果是四个边上的O那么就设置为B且与之相连O也设置为B
        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                dfs(row - 1, j)
        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][col-1] == "O":
                dfs(i, col - 1)

        # 再循环一遍 O变成X B变成O
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"
```

# [695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/ "695. 岛屿的最大面积")
```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def infection(r, c):
            if r< 0 or r > row-1 or c< 0 or c > col-1 or grid[r][c] != 1:
                return 0
            grid[r][c] = 2
            return 1 + infection(r-1,c) + infection(r+1,c) + infection(r,c-1) + infection(r,c+1)
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    count = max(infection(r,c),count)
        return count

```
# [417. 太平洋大西洋水流问题](https://leetcode-cn.com/problems/pacific-atlantic-water-flow/ "417. 太平洋大西洋水流问题")
```python
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        row, col = len(matrix), len(matrix[0])
        to = [(-1,0),(0,-1),(1,0),(0,1)]
        # 构建分别可以到达两个位置的集合
        tpy = set()
        dxy = set()
        def dfs(r ,c, res):
            # 因为集合即使坐标存在也不会重复加入
            res.add((r, c))
            for i, j in to:
                new_r = r + i
                new_c = c + j
                # 不越界 且 符合高到低或同等的高度流动原则
                if 0<=new_r<row and 0<=new_c<col and matrix[r][c] <= matrix[new_r][new_c] and (new_r,new_c) not in res:
                    dfs(new_r, new_c,res)

        # 从四个边界遍历如果比上一个小就以到达加入答案中
        for c in range(col):
            dfs(0, c ,tpy)
            dfs(row-1, c, dxy)
        for r in range(row):
            dfs(r, 0, tpy)
            dfs(r, col-1,dxy)
        # 取 能到太平洋和能到大西洋的交集
        return [list(i) for i in tpy&dxy]
```