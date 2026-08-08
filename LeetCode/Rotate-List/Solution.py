1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def rotateRight(self, head, k):
9        if not head or not head.next:
10            return head
11        
12        # 1. Find length and tail
13        length = 1
14        tail = head
15        while tail.next:
16            tail = tail.next
17            length += 1
18        
19        # 2. Make circular
20        tail.next = head
21        
22        # 3. Effective rotation (k can be huge)
23        k = k % length
24        
25        # 4. Find new tail: (length - k) steps from head
26        steps = length - k
27        new_tail = head
28        for _ in range(steps - 1):
29            new_tail = new_tail.next
30        
31        # 5. Break the circle
32        new_head = new_tail.next
33        new_tail.next = None
34        
35        return new_head