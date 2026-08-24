1class Solution(object):
2    def invertTree(self, root):
3        """
4        :type root: TreeNode
5        :rtype: TreeNode
6        """
7        if root is None:
8            return None
9        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
10        return root