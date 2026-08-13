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
18        while leftmost.left:
19            head = leftmost
20            
21            while head:
22                # Connect left child to right child
23                head.left.next = head.right
24                
25                # Connect right child to next node's left child
26                if head.next:
27                    head.right.next = head.next.left
28                
29                head = head.next
30            
31            # Move to next level
32            leftmost = leftmost.left
33        
34        return root