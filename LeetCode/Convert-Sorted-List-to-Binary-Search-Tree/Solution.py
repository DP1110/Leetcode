1class Solution:
2    def sortedListToBST(self, head):
3        if not head:
4            return None
5        if not head.next:
6            return TreeNode(head.val)
7        
8        # Find middle using slow/fast pointers
9        prev_slow = None
10        slow = head
11        fast = head
12        while fast and fast.next:
13            prev_slow = slow
14            slow = slow.next
15            fast = fast.next.next
16        
17        # Disconnect left half
18        prev_slow.next = None
19        
20        root = TreeNode(slow.val)
21        root.left = self.sortedListToBST(head)
22        root.right = self.sortedListToBST(slow.next)
23        return root