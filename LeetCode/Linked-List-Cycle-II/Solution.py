1class Solution:
2    def detectCycle(self, head):
3        slow = fast = head
4
5        # Phase 1: detect cycle
6        while fast and fast.next:
7            slow = slow.next
8            fast = fast.next.next
9            if slow == fast:
10                break
11        else:
12            return None  # no cycle
13
14        # Phase 2: find cycle start
15        ptr = head
16        while ptr != slow:
17            ptr = ptr.next
18            slow = slow.next
19
20        return ptr