# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next       # Node 1
            second = prev.next.next # Node 2
            
            # Rewire: prev → second → first → rest
            prev.next = second
            first.next = second.next
            second.next = first
            
            # Move prev forward for next pair
            prev = first
        
        return dummy.next