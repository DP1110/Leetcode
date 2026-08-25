1class Solution(object):
2    def lowestCommonAncestor(self, root, p, q):
3        """
4        :type root: TreeNode
5        :type p: TreeNode
6        :type q: TreeNode
7        :rtype: TreeNode
8        """
9        if root is None or root == p or root == q:
10            return root
11        left = self.lowestCommonAncestor(root.left, p, q)
12        right = self.lowestCommonAncestor(root.right, p, q)
13        if left and right:
14            return root
15        return left if left else right
16        