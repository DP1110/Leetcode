1class Solution(object):
2    def productExceptSelf(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        n = len(nums)
8        res = [1]*n
9        for i in xrange(1, n):
10            res[i] = res[i-1]*nums[i-1]
11        suf = 1
12        for i in xrange(n-1, -1, -1):
13            res[i] *= suf
14            suf *= nums[i]
15        return res