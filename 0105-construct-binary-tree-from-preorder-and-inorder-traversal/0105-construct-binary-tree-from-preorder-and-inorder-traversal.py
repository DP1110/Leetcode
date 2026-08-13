# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # Map each value to its index in inorder
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i
        
        self.pre_idx = 0  # tracks current position in preorder
        
        def helper(in_left, in_right):
            # No elements in this subtree
            if in_left > in_right:
                return None
            
            # Current root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            # Root's position in inorder splits left/right subtrees
            in_idx = inorder_map[root_val]
            
            # Build left subtree first (preorder is root → left → right)
            root.left = helper(in_left, in_idx - 1)
            root.right = helper(in_idx + 1, in_right)
            
            return root
        
        return helper(0, len(inorder) - 1)