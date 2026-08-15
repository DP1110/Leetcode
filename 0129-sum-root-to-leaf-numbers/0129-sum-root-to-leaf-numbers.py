class Solution(object):
    def sumNumbers(self, root):
        def dfs(node, current):
            if not node:
                return 0
            
            current = current * 10 + node.val
            
            # Leaf node: return the complete number
            if not node.left and not node.right:
                return current
            
            # Recurse on children
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)