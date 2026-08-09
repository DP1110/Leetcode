# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        
        # 1. Find length and tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # 2. Make circular
        tail.next = head
        
        # 3. Effective rotation (k can be huge)
        k = k % length
        
        # 4. Find new tail: (length - k) steps from head
        steps = length - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        
        # 5. Break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head