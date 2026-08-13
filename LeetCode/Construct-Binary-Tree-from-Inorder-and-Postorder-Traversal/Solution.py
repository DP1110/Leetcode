1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def buildTree(self, inorder, postorder):
10        inorder_map = {}
11        for i, val in enumerate(inorder):
12            inorder_map[val] = i
13        
14        self.post_idx = len(postorder) - 1
15        
16        def helper(in_left, in_right):
17            if in_left > in_right:
18                return None
19            
20            # Current root from postorder (from the end)
21            root_val = postorder[self.post_idx]
22            self.post_idx -= 1
23            root = TreeNode(root_val)
24            
25            # Root's position in inorder
26            in_idx = inorder_map[root_val]
27            
28            # Build RIGHT first, then LEFT (postorder is L-R-Root, so reverse is Root-R-L)
29            root.right = helper(in_idx + 1, in_right)
30            root.left = helper(in_left, in_idx - 1)
31            
32            return root
33        
34        return helper(0, len(inorder) - 1)