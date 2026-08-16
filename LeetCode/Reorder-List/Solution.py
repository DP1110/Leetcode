1class Solution:
2    def reorderList(self, head):
3        if not head or not head.next:
4            return
5
6        # Step 1: find middle (slow at mid after loop)
7        slow, fast = head, head
8        while fast.next and fast.next.next:
9            slow = slow.next
10            fast = fast.next.next
11
12        # Step 2: reverse second half
13        second = slow.next
14        slow.next = None
15        prev = None
16        while second:
17            nxt = second.next
18            second.next = prev
19            prev = second
20            second = nxt
21        second = prev
22
23        # Step 3: merge two halves alternately
24        first = head
25        while second:
26            n1 = first.next
27            n2 = second.next
28            first.next = second
29            second.next = n1
30            first = n1
31            second = n2