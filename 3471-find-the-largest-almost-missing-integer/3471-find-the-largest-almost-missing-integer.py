class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        distinct_vals = set(nums)
        result = -1

        for x in distinct_vals:
            window_count = 0
            for start in range(n - k + 1):
                if x in nums[start:start + k]:
                    window_count += 1
                if window_count > 1:
                    break

            if window_count == 1:
                if x > result:
                    result = x

        return result