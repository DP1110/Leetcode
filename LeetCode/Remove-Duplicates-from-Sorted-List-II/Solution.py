1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def deleteDuplicates(self, head):
9        dummy = ListNode(0)
10        dummy.next = head
11        
12        prev = dummy
13        
14        while head:
15            # If current node has duplicates ahead
16            if head.next and head.val == head.next.val:
17                # Remember the duplicate value
18                val = head.val
19                # Skip all nodes with this value
20                while head and head.val == val:
21                    head = head.next
22                # Link prev to the next distinct node
23                prev.next = head
24            else:
25                # No duplicate — current node is safe
26                prev = head
27                head = head.next
28        
29        return dummy.next