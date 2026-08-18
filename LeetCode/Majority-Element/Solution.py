1class Solution(object):
2    def majorityElement(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        count = 0
8        candidate = None
9
10        for n in nums:
11            if count == 0:
12                candidate = n
13            count += 1 if n == candidate else -1
14
15        return candidate