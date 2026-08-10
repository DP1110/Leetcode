class Solution(object):
    def subsets(self, nums):
        res = []
        path = []

        def backtrack(start):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res