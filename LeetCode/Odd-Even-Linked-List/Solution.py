1class Solution(object):
2    def oddEvenList(self, head):
3        if not head or not head.next:
4            return head
5        odd = head
6        even = head.next
7        even_head = even
8        while even and even.next:
9            odd.next = even.next
10            odd = odd.next
11            even.next = odd.next
12            even = even.next
13        odd.next = even_head
14        return head