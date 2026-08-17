1class Solution(object):
2    def findMin(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        lo, hi = 0, len(nums) - 1
8
9        while lo < hi:
10            mid = (lo + hi) // 2
11            if nums[mid] > nums[hi]:
12                lo = mid + 1
13            elif nums[mid] < nums[hi]:
14                hi = mid
15            else:
16                hi -= 1  # dup, shrink safe side
17
18        return nums[lo]