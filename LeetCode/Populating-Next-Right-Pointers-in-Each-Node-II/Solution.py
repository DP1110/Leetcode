1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val=0, left=None, right=None, next=None):
5        self.val = val
6        self.left = left
7        self.right = right
8        self.next = next
9"""
10
11class Solution:
12    def connect(self, root):
13        if not root:
14            return None
15        
16        leftmost = root
17        
18        while leftmost:
19            # Dummy head for the next level
20            dummy = Node(0)
21            tail = dummy
22            
23            # Traverse current level
24            curr = leftmost
25            while curr:
26                if curr.left:
27                    tail.next = curr.left
28                    tail = tail.next
29                if curr.right:
30                    tail.next = curr.right
31                    tail = tail.next
32                curr = curr.next
33            
34            # Move to next level
35            leftmost = dummy.next
36        
37        return root