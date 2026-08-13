1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def minDepth(self, root):
10        if not root:
11            return 0
12        
13        from collections import deque
14        queue = deque([(root, 1)])
15        
16        while queue:
17            node, depth = queue.popleft()
18            
19            # Check if leaf node
20            if not node.left and not node.right:
21                return depth
22            
23            if node.left:
24                queue.append((node.left, depth + 1))
25            if node.right:
26                queue.append((node.right, depth + 1))
27        
28        return 0