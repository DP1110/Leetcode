1
2
3class Solution:
4    def reverseKGroup(self, head, k):
5        dummy = ListNode(0, head)
6        group_prev = dummy
7        
8        while True:
9            # Check if there are k nodes remaining
10            kth = group_prev
11            for _ in range(k):
12                kth = kth.next
13                if not kth:
14                    return dummy.next
15            group_next = kth.next
16            
17            # Reverse the k nodes: group_prev.next ... kth
18            prev_node = group_next   # Will become the successor of the new tail
19            curr = group_prev.next   # First node of current group
20            
21            while curr != group_next:
22                nxt = curr.next
23                curr.next = prev_node
24                prev_node = curr
25                curr = nxt
26            
27            # Move group_prev to the tail of the just-reversed group
28            temp = group_prev.next   # Old head, now tail
29            group_prev.next = kth    # New head
30            group_prev = temp