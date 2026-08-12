# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Move prev to the node before position left
        for _ in range(left - 1):
            prev = prev.next
        
        # curr is the first node of the sublist to be reversed
        curr = prev.next
        
        # Reverse the sublist from left to right
        # Standard iterative reversal but only for (right - left) steps
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next