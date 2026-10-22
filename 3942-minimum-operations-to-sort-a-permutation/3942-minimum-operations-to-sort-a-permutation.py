class Solution:
    def minOperations(self, nums):
        n = len(nums)
        k = nums[0]
        INF = float("inf")
        best = INF

        # Case A: ascending rotation
        if all(nums[(i + 1) % n] == (nums[i] + 1) % n for i in range(n)):
            if k == 0:
                return 0
            best = min(best, (n - k) % n, k + 2)

        # Case B: descending rotation
        if all(nums[(i + 1) % n] == (nums[i] - 1) % n for i in range(n)):
            j = (k + 1) % n
            best = min(best, 1 + j, 1 + (n - j) % n)

        return -1 if best == INF else best