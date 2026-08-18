1class Solution(object):
2    def findPeakElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        lo, hi = 0, len(nums) - 1
8
9        while lo < hi:
10            mid = (lo + hi) // 2
11            if nums[mid] < nums[mid + 1]:
12                lo = mid + 1  # peak on right side
13            else:
14                hi = mid  # peak at mid or left side
15
16        return lo