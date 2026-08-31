class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        first = prev_idx = None
        last = -1
        prev = head
        cur = head.next
        idx = 1
        min_dist = float('inf')

        while cur.next:
            if (cur.val > prev.val and cur.val > cur.next.val) or (cur.val < prev.val and cur.val < cur.next.val):
                if first is None:
                    first = idx
                else:
                    min_dist = min(min_dist, idx - last)
                last = idx
            prev = cur
            cur = cur.next
            idx += 1

        if first is None or first == last:
            return [-1, -1]
        return [min_dist, last - first]