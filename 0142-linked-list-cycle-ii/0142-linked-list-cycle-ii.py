class Solution:
    def detectCycle(self, head):
        slow = fast = head

        # Phase 1: detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # no cycle

        # Phase 2: find cycle start
        ptr = head
        while ptr != slow:
            ptr = ptr.next
            slow = slow.next

        return ptr