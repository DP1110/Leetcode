class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        new_head = head.next
        copy_curr = new_head
        while curr:
            curr.next = curr.next.next
            copy_curr.next = copy_curr.next.next if copy_curr.next else None
            curr = curr.next
            copy_curr = copy_curr.next

        return new_head