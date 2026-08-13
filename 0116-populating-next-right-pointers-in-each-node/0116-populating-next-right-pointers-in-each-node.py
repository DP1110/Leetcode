"""
# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        if not root:
            return None
        
        leftmost = root
        
        while leftmost.left:
            head = leftmost
            
            while head:
                # Connect left child to right child
                head.left.next = head.right
                
                # Connect right child to next node's left child
                if head.next:
                    head.right.next = head.next.left
                
                head = head.next
            
            # Move to next level
            leftmost = leftmost.left
        
        return root