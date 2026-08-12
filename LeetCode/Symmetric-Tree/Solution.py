1class Solution(object):
2    def isSymmetric(self, root):
3        if not root:
4            return True
5        return self.isMirror(root.left, root.right)
6    
7    def isMirror(self, left, right):
8        if not left and not right:
9            return True
10        if not left or not right:
11            return False
12        return (left.val == right.val and 
13                self.isMirror(left.left, right.right) and 
14                self.isMirror(left.right, right.left))