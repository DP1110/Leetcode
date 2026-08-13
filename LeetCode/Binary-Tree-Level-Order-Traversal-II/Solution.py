1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def levelOrderBottom(self, root):
10        if not root:
11            return []
12        
13        from collections import deque
14        queue = deque([root])
15        result = []
16        
17        while queue:
18            level_size = len(queue)
19            level = []
20            for _ in range(level_size):
21                node = queue.popleft()
22                level.append(node.val)
23                if node.left:
24                    queue.append(node.left)
25                if node.right:
26                    queue.append(node.right)
27            result.append(level)
28        
29        # Reverse to get bottom-up order
30        result.reverse()
31        return result