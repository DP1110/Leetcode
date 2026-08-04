1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def swapPairs(self, head):
9        dummy = ListNode(0)
10        dummy.next = head
11        prev = dummy
12        
13        while prev.next and prev.next.next:
14            first = prev.next       # Node 1
15            second = prev.next.next # Node 2
16            
17            # Rewire: prev → second → first → rest
18            prev.next = second
19            first.next = second.next
20            second.next = first
21            
22            # Move prev forward for next pair
23            prev = first
24        
25        return dummy.next