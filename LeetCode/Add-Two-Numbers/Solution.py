1class Solution:
2    def addTwoNumbers(self, l1, l2):
3        dummy = ListNode()
4        current = dummy
5        carry = 0
6        while l1 or l2 or carry:
7            val1 = l1.val if l1 else 0
8            val2 = l2.val if l2 else 0
9            total = val1 + val2 + carry
10            carry = total // 10
11            current.next = ListNode(total % 10)
12            current = current.next
13            l1 = l1.next if l1 else None
14            l2 = l2.next if l2 else None
15        return dummy.next