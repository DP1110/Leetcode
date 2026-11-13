from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = deque()
        r = n - 1
        cost = 0
        ans = 0
        for l in range(n - 1, -1, -1):
            v = nums[l]
            while dq and nums[dq[0]] <= v:
                j = dq.popleft()
                nxt = dq[0] if dq else r + 1
                cost += (v - nums[j]) * (nxt - j)
            dq.appendleft(l)
            while cost > k:
                b = dq[-1]
                cost -= nums[b] - nums[r]
                if b == r:
                    dq.pop()
                r -= 1
            ans += r - l + 1
        return ans