class Solution(object):
    def smallestIndex(self, nums):
        for i, x in enumerate(nums):
            if sum(int(d) for d in str(x)) == i:
                return i
        return -1