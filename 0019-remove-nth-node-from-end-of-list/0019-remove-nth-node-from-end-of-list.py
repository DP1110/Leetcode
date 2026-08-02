# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        fast = slow = dummy
        
        # Move fast n+1 steps ahead (to land slow right before target)
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both until fast hits the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Skip the nth node from end
        slow.next = slow.next.next
        
        return dummy.next