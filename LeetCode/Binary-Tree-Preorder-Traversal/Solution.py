1class Solution:
2    def preorderTraversal(self, root):
3        result = []
4
5        def dfs(node):
6            if not node:
7                return
8            result.append(node.val)
9            dfs(node.left)
10            dfs(node.right)
11
12        dfs(root)
13        return result