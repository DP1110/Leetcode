1class Solution(object):
2    def deleteNode(self, node):
3        """
4        :type node: ListNode
5        :rtype: None Do not return anything, modify node in-place instead.
6        """
7        node.val = node.next.val
8        node.next = node.next.next