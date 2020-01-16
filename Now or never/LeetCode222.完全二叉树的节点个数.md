# [LeetCode222. 完全二叉树的节点个数.md](https://leetcode-cn.com/problems/count-complete-tree-nodes/ "LeetCode222. 完全二叉树的节点个数.md")
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

要求:
时间复杂度低于O(n)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def get_num(head):
            if not head:
                return 0
            return helper(head, 1, most_left_level(head, 1))


        def most_left_level(node, level):
            while node:
                level += 1
                node = node.left
            return level - 1


        def helper(node, level, high):
            if level == high:
                return 1
            if most_left_level(node.right, level + 1) == high:  # 右子树的左边界到了哪一层
                return 2 ** (high - level) + helper(node.right, level + 1, high)
            else:
                return helper(node.left, level + 1, high) + 2 ** (high - level - 1)
        return get_num(root)
```
或者
```python
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        left_height = 0
        left_node = root
        right_height = 0
        right_node = root
        while left_node:
            left_node = left_node.left
            left_height += 1
        while right_node:
            right_node = right_node.right
            right_height += 1
        if left_height == right_height:
            return (2**left_height) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
```