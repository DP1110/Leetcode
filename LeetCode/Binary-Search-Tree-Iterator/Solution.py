1class BSTIterator(object):
2
3    def __init__(self, root):
4        """
5        :type root: TreeNode
6        """
7        self.stack = []
8        self._push_left(root)
9
10    def _push_left(self, node):
11        while node:
12            self.stack.append(node)
13            node = node.left
14
15    def next(self):
16        """
17        :rtype: int
18        """
19        node = self.stack.pop()
20        if node.right:
21            self._push_left(node.right)
22        return node.val
23
24    def hasNext(self):
25        """
26        :rtype: bool
27        """
28        return len(self.stack) > 0