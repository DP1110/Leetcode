1class Solution(object):
2    def recoverTree(self, root):
3        first = second = prev = None
4        curr = root
5
6        while curr:
7            if curr.left is None:
8                # visit curr
9                if prev and prev.val > curr.val:
10                    if first is None:
11                        first = prev
12                    second = curr
13                prev = curr
14                curr = curr.right
15            else:
16                # find inorder predecessor
17                pred = curr.left
18                while pred.right and pred.right is not curr:
19                    pred = pred.right
20
21                if pred.right is None:
22                    pred.right = curr  # create thread
23                    curr = curr.left
24                else:
25                    pred.right = None  # remove thread
26                    # visit curr
27                    if prev and prev.val > curr.val:
28                        if first is None:
29                            first = prev
30                        second = curr
31                    prev = curr
32                    curr = curr.right
33
34        first.val, second.val = second.val, first.val