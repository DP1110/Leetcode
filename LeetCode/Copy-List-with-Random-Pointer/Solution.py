1class Solution:
2    def copyRandomList(self, head):
3        if not head:
4            return None
5
6        curr = head
7        while curr:
8            copy = Node(curr.val)
9            copy.next = curr.next
10            curr.next = copy
11            curr = copy.next
12
13        curr = head
14        while curr:
15            if curr.random:
16                curr.next.random = curr.random.next
17            curr = curr.next.next
18
19        curr = head
20        new_head = head.next
21        copy_curr = new_head
22        while curr:
23            curr.next = curr.next.next
24            copy_curr.next = copy_curr.next.next if copy_curr.next else None
25            curr = curr.next
26            copy_curr = copy_curr.next
27
28        return new_head