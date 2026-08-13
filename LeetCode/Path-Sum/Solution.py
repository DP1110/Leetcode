1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def hasPathSum(self, root, targetSum):
10        if not root:
11            return False
12        
13        # Check if leaf node
14        if not root.left and not root.right:
15            return root.val == targetSum
16        
17        # Recurse on children with reduced target
18        remaining = targetSum - root.val
19        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)