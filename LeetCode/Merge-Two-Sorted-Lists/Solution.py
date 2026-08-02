1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def mergeTwoLists(self, list1, list2):
9        dummy = ListNode(0)
10        tail = dummy
11        
12        while list1 and list2:
13            if list1.val <= list2.val:
14                tail.next = list1
15                list1 = list1.next
16            else:
17                tail.next = list2
18                list2 = list2.next
19            tail = tail.next
20        
21        # Attach remaining nodes
22        tail.next = list1 if list1 else list2
23        
24        return dummy.next