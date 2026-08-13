1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def maxDepth(self, root):
10        if not root:
11            return 0
12        left_depth = self.maxDepth(root.left)
13        right_depth = self.maxDepth(root.right)
14        return 1 + max(left_depth, right_depth)