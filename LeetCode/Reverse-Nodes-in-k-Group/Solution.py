1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseKGroup(self, head, k):
9        dummy = ListNode(0, head)
10        group_prev = dummy
11        
12        while True:
13            # Check if there are k nodes remaining
14            kth = group_prev
15            for _ in range(k):
16                kth = kth.next
17                if not kth:
18                    return dummy.next
19            group_next = kth.next
20            
21            # Reverse the k nodes: group_prev.next ... kth
22            prev_node = group_next   # Will become the successor of the new tail
23            curr = group_prev.next   # First node of current group
24            
25            while curr != group_next:
26                nxt = curr.next
27                curr.next = prev_node
28                prev_node = curr
29                curr = nxt
30            
31            # Move group_prev to the tail of the just-reversed group
32            temp = group_prev.next   # Old head, now tail
33            group_prev.next = kth    # New head
34            group_prev = temp