1class Solution(object):
2    def countNodes(self, root):
3        if not root:
4            return 0
5
6        def left_height(node):
7            h = 0
8            while node:
9                h += 1
10                node = node.left
11            return h
12
13        def right_height(node):
14            h = 0
15            while node:
16                h += 1
17                node = node.right
18            return h
19
20        lh = left_height(root)
21        rh = right_height(root)
22        if lh == rh:
23            return (1 << lh) - 1
24        return 1 + self.countNodes(root.left) + self.countNodes(root.right)