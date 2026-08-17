1class Solution(object):
2    def maxProduct(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        cur_max = nums[0]
8        cur_min = nums[0]
9        result = nums[0]
10
11        for i in range(1, len(nums)):
12            n = nums[i]
13            if n < 0:
14                cur_max, cur_min = cur_min, cur_max
15
16            cur_max = max(n, cur_max * n)
17            cur_min = min(n, cur_min * n)
18
19            result = max(result, cur_max)
20
21        return result