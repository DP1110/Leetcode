1class Solution(object):
2    def rightSideView(self, root):
3        if not root:
4            return []
5        res = []
6        queue = [root]
7        while queue:
8            res.append(queue[-1].val)
9            nxt = []
10            for node in queue:
11                if node.left:
12                    nxt.append(node.left)
13                if node.right:
14                    nxt.append(node.right)
15            queue = nxt
16        return res