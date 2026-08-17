class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max = nums[0]
        cur_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            if n < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)

            result = max(result, cur_max)

        return result