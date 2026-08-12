
class Solution:
    def partition(self, head, x):
        # Dummy heads for the two partitions
        less_dummy    = ListNode(0)
        greater_dummy = ListNode(0)
        
        less    = less_dummy      # tail of the < x chain
        greater = greater_dummy   # tail of the >= x chain
        
        current = head
        while current:
            if current.val < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next
        
        # Connect: less chain -> greater chain -> None
        less.next = greater_dummy.next
        greater.next = None
        
        return less_dummy.next