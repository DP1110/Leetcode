1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def mergeKLists(self, lists):
9        if not lists:
10            return None
11        
12        # Iteratively merge lists in pairs
13        while len(lists) > 1:
14            merged = []
15            for i in range(0, len(lists), 2):
16                l1 = lists[i]
17                l2 = lists[i + 1] if i + 1 < len(lists) else None
18                merged.append(self.mergeTwoLists(l1, l2))
19            lists = merged
20        
21        return lists[0]
22    
23    def mergeTwoLists(self, l1, l2):
24        dummy = ListNode(0)
25        tail = dummy
26        
27        while l1 and l2:
28            if l1.val <= l2.val:
29                tail.next = l1
30                l1 = l1.next
31            else:
32                tail.next = l2
33                l2 = l2.next
34            tail = tail.next
35        
36        tail.next = l1 if l1 else l2
37        return dummy.next