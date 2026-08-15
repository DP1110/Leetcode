# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i
        
        self.post_idx = len(postorder) - 1
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            # Current root from postorder (from the end)
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            
            # Root's position in inorder
            in_idx = inorder_map[root_val]
            
            # Build RIGHT first, then LEFT (postorder is L-R-Root, so reverse is Root-R-L)
            root.right = helper(in_idx + 1, in_right)
            root.left = helper(in_left, in_idx - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)