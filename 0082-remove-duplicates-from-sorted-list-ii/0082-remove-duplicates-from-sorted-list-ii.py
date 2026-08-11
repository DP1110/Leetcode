# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        while head:
            # If current node has duplicates ahead
            if head.next and head.val == head.next.val:
                # Remember the duplicate value
                val = head.val
                # Skip all nodes with this value
                while head and head.val == val:
                    head = head.next
                # Link prev to the next distinct node
                prev.next = head
            else:
                # No duplicate — current node is safe
                prev = head
                head = head.next
        
        return dummy.next