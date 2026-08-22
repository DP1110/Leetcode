1class Solution(object):
2    def reverseList(self, head):
3        prev = None
4        while head:
5            nxt = head.next
6            head.next = prev
7            prev = head
8            head = nxt
9        return prev