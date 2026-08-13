1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def __init__(self):
10        self.prev = None
11    
12    def flatten(self, root):
13        if not root:
14            return
15        
16        # Reverse pre-order: right, left, root
17        self.flatten(root.right)
18        self.flatten(root.left)
19        
20        # Stitch current node to the already-flattened suffix
21        root.right = self.prev
22        root.left = None
23        self.prev = root