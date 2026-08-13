1class Solution:
2    def __init__(self):
3        self.prev = None
4    
5    def flatten(self, root):
6        if not root:
7            return
8        
9        self.flatten(root.right)
10        self.flatten(root.left)
11        
12        root.right = self.prev
13        root.left = None
14        self.prev = root