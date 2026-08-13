1class Solution(object):
2    def maxPathSum(self, root):
3        self.best = float('-inf')
4        
5        def gain(node):
6            if not node:
7                return 0
8            left = max(gain(node.left), 0)
9            right = max(gain(node.right), 0)
10            self.best = max(self.best, node.val + left + right)
11            return node.val + max(left, right)
12        
13        gain(root)
14        return self.best