1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def zigzagLevelOrder(self, root):
10        if not root:
11            return []
12        
13        from collections import deque
14        queue = deque([root])
15        result = []
16        left_to_right = True
17        
18        while queue:
19            level_size = len(queue)
20            level = []
21            
22            for _ in range(level_size):
23                node = queue.popleft()
24                level.append(node.val)
25                if node.left:
26                    queue.append(node.left)
27                if node.right:
28                    queue.append(node.right)
29            
30            if not left_to_right:
31                level.reverse()
32            
33            result.append(level)
34            left_to_right = not left_to_right
35        
36        return result