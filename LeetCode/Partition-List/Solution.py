1
2class Solution:
3    def partition(self, head, x):
4        # Dummy heads for the two partitions
5        less_dummy    = ListNode(0)
6        greater_dummy = ListNode(0)
7        
8        less    = less_dummy      # tail of the < x chain
9        greater = greater_dummy   # tail of the >= x chain
10        
11        current = head
12        while current:
13            if current.val < x:
14                less.next = current
15                less = less.next
16            else:
17                greater.next = current
18                greater = greater.next
19            current = current.next
20        
21        # Connect: less chain -> greater chain -> None
22        less.next = greater_dummy.next
23        greater.next = None
24        
25        return less_dummy.next