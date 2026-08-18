1class Solution(object):
2    def getIntersectionNode(self, headA, headB):
3        """
4        :type head1, head1: ListNode
5        :rtype: ListNode
6        """
7        pa, pb = headA, headB
8
9        while pa != pb:
10            pa = pa.next if pa else headB
11            pb = pb.next if pb else headA
12
13        return pa