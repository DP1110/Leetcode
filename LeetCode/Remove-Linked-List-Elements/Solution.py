1class Solution(object):
2    def removeElements(self, head, val):
3        dummy = ListNode(0)
4        dummy.next = head
5        curr = dummy
6        while curr.next:
7            if curr.next.val == val:
8                curr.next = curr.next.next
9            else:
10                curr = curr.next
11        return dummy.next