class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if n == candidate else -1

        return candidate