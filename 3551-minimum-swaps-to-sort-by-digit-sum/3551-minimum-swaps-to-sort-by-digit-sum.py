class Solution(object):
    def minSwaps(self, nums):
        n = len(nums)
        key = lambda i: (sum(map(int, str(nums[i]))), nums[i])
        order = sorted(range(n), key=key)
        # order[k] = original index of element that belongs at position k
        pos = [0] * n
        for k, i in enumerate(order):
            pos[i] = k
        seen = [False] * n
        cycles = 0
        for i in range(n):
            if not seen[i]:
                cycles += 1
                while not seen[i]:
                    seen[i] = True
                    i = pos[i]
        return n - cycles