1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def pathSum(self, root, targetSum):
10        result = []
11        path = []
12        
13        def dfs(node, remaining):
14            if not node:
15                return
16            
17            path.append(node.val)
18            
19            # Check leaf
20            if not node.left and not node.right:
21                if node.val == remaining:
22                    result.append(path[:])  # copy
23            
24            dfs(node.left, remaining - node.val)
25            dfs(node.right, remaining - node.val)
26            
27            path.pop()  # backtrack
28        
29        dfs(root, targetSum)
30        return result