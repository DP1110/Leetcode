class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        curr = root
        
        while curr or stack:
            # Go all the way left
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process node
            curr = stack.pop()
            result.append(curr.val)
            
            # Go right
            curr = curr.right
        
        return result