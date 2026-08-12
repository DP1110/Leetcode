class Solution(object):
    def isSameTree(self, p, q):
        # Both empty
        if not p and not q:
            return True
        
        # One empty, one not
        if not p or not q:
            return False
        
        # Values differ
        if p.val != q.val:
            return False
        
        # Recurse on both subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)