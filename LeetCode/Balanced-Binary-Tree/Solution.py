1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def isBalanced(self, root):
10        def check(node):
11            if not node:
12                return 0
13            
14            left = check(node.left)
15            if left == -1:
16                return -1
17            
18            right = check(node.right)
19            if right == -1:
20                return -1
21            
22            if abs(left - right) > 1:
23                return -1
24            
25            return max(left, right) + 1
26        
27        return check(root) != -1