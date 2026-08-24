1class Solution(object):
2    def kthSmallest(self, root, k):
3        """
4        :type root: TreeNode
5        :type k: int
6        :rtype: int
7        """
8        stack = []
9        node = root
10        while stack or node:
11            while node:
12                stack.append(node)
13                node = node.left
14            node = stack.pop()
15            k -= 1
16            if k == 0:
17                return node.val
18            node = node.right