1class Solution(object):
2    def wiggleSort(self, nums):
3        n = len(nums)
4        s = sorted(nums)
5        half = (n + 1) // 2
6        small = s[:half][::-1]
7        large = s[half:][::-1]
8        for i in range(half):
9            nums[2*i] = small[i]
10        for i in range(n - half):
11            nums[2*i + 1] = large[i]