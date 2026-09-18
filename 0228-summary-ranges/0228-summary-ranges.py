class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        i = 0
        while i < n:
            j = i
            while j+1 < n and nums[j+1] == nums[j]+1:
                j += 1
            if i == j:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + "->" + str(nums[j]))
            i = j+1
        return res