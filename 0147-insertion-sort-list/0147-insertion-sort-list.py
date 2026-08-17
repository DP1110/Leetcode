class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = head

        while cur:
            nxt = cur.next  # save next before rewire

            p = dummy
            while p.next and p.next.val < cur.val:
                p = p.next

            cur.next = p.next
            p.next = cur

            cur = nxt

        return dummy.next