1class Solution(object):
2    def isSameTree(self, p, q):
3        # Both empty
4        if not p and not q:
5            return True
6        
7        # One empty, one not
8        if not p or not q:
9            return False
10        
11        # Values differ
12        if p.val != q.val:
13            return False
14        
15        # Recurse on both subtrees
16        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)