1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def buildTree(self, preorder, inorder):
10        # Map each value to its index in inorder
11        inorder_map = {}
12        for i, val in enumerate(inorder):
13            inorder_map[val] = i
14        
15        self.pre_idx = 0  # tracks current position in preorder
16        
17        def helper(in_left, in_right):
18            # No elements in this subtree
19            if in_left > in_right:
20                return None
21            
22            # Current root from preorder
23            root_val = preorder[self.pre_idx]
24            self.pre_idx += 1
25            root = TreeNode(root_val)
26            
27            # Root's position in inorder splits left/right subtrees
28            in_idx = inorder_map[root_val]
29            
30            # Build left subtree first (preorder is root → left → right)
31            root.left = helper(in_left, in_idx - 1)
32            root.right = helper(in_idx + 1, in_right)
33            
34            return root
35        
36        return helper(0, len(inorder) - 1)