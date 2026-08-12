1class Solution(object):
2    def isValidBST(self, root):
3        def validate(node, lower, upper):
4            if not node:
5                return True
6            
7            # Check bounds
8            if lower is not None and node.val <= lower:
9                return False
10            if upper is not None and node.val >= upper:
11                return False
12            
13            # Recurse: left gets upper=node.val, right gets lower=node.val
14            return validate(node.left, lower, node.val) and \
15                   validate(node.right, node.val, upper)
16        
17        return validate(root, None, None)