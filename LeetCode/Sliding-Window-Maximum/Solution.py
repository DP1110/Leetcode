1from collections import deque
2
3class Solution(object):
4    def maxSlidingWindow(self, nums, k):
5        """
6        :type nums: List[int]
7        :type k: int
8        :rtype: List[int]
9        """
10        dq = deque()
11        res = []
12        for i, x in enumerate(nums):
13            while dq and nums[dq[-1]] <= x:
14                dq.pop()
15            dq.append(i)
16            if dq[0] <= i-k:
17                dq.popleft()
18            if i >= k-1:
19                res.append(nums[dq[0]])
20        return res