1class Solution(object):
2    def insertionSortList(self, head):
3        """
4        :type head: ListNode
5        :rtype: ListNode
6        """
7        dummy = ListNode(0)
8        cur = head
9
10        while cur:
11            nxt = cur.next  # save next before rewire
12
13            p = dummy
14            while p.next and p.next.val < cur.val:
15                p = p.next
16
17            cur.next = p.next
18            p.next = cur
19
20            cur = nxt
21
22        return dummy.next