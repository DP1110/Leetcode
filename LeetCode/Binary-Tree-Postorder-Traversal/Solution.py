1class Solution:
2    def postorderTraversal(self, root):
3        result = []
4
5        def dfs(node):
6            if not node:
7                return
8            dfs(node.left)
9            dfs(node.right)
10            result.append(node.val)
11
12        dfs(root)
13        return result