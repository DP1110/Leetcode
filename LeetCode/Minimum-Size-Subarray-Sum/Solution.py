1class Solution(object):
2    def minSubArrayLen(self, target, nums):
3        left = 0
4        total = 0
5        min_len = float('inf')
6        for right in range(len(nums)):
7            total += nums[right]
8            while total >= target:
9                min_len = min(min_len, right - left + 1)
10                total -= nums[left]
11                left += 1
12        return min_len if min_len != float('inf') else 0