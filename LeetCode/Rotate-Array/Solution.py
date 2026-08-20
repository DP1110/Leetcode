1class Solution(object):
2    def rotate(self, nums, k):
3        n = len(nums)
4        k %= n
5        def reverse(l, r):
6            while l < r:
7                nums[l], nums[r] = nums[r], nums[l]
8                l += 1
9                r -= 1
10        reverse(0, n - 1)
11        reverse(0, k - 1)
12        reverse(k, n - 1)