class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: find middle (slow at mid after loop)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        second = prev

        # Step 3: merge two halves alternately
        first = head
        while second:
            n1 = first.next
            n2 = second.next
            first.next = second
            second.next = n1
            first = n1
            second = n2