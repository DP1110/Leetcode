1class Solution:
2    def firstMissingPositive(self, nums):
3        n = len(nums)
4        for i in range(n):
5            v = nums[i]
6            while 1 <= v <= n and nums[v - 1] != v:
7                j = v - 1
8                nums[i], nums[j] = nums[j], nums[i]
9                v = nums[i]
10
11        for i in range(n):
12            if nums[i] != i + 1:
13                return i + 1
14        return n + 1