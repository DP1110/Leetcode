1class Solution:
2    def hasCycle(self, head):
3        slow = fast = head
4
5        while fast and fast.next:
6            slow = slow.next
7            fast = fast.next.next
8            if slow == fast:
9                return True
10
11        return False