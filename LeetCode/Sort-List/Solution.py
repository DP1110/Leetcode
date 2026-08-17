1class Solution(object):
2    def sortList(self, head):
3        """
4        :type head: ListNode
5        :rtype: ListNode
6        """
7        if not head or not head.next:
8            return head
9
10        # split: slow/fast, slow lands at mid
11        slow, fast = head, head.next
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15
16        mid = slow.next
17        slow.next = None  # cut
18
19        left = self.sortList(head)
20        right = self.sortList(mid)
21
22        return self._merge(left, right)
23
24    def _merge(self, l1, l2):
25        dummy = ListNode(0)
26        tail = dummy
27
28        while l1 and l2:
29            if l1.val <= l2.val:
30                tail.next = l1
31                l1 = l1.next
32            else:
33                tail.next = l2
34                l2 = l2.next
35            tail = tail.next
36
37        tail.next = l1 if l1 else l2
38
39        return dummy.next