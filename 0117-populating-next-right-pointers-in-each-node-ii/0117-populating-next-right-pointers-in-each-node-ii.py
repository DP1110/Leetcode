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
        
        while leftmost:
            # Dummy head for the next level
            dummy = Node(0)
            tail = dummy
            
            # Traverse current level
            curr = leftmost
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            
            # Move to next level
            leftmost = dummy.next
        
        return root