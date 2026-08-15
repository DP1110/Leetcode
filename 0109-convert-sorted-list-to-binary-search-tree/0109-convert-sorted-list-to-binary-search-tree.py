class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        # Find middle using slow/fast pointers
        prev_slow = None
        slow = head
        fast = head
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        
        # Disconnect left half
        prev_slow.next = None
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root