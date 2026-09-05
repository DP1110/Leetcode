import random

class Solution(object):
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        result = None
        node = self.head
        i = 0
        while node:
            i += 1
            if random.randint(1, i) == 1:
                result = node.val
            node = node.next
        return result