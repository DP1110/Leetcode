1class Solution(object):
2    def resultArray(self, nums):
3        a1 = [nums[0]]
4        a2 = [nums[1]]
5        for x in nums[2:]:
6            if a1[-1] > a2[-1]:
7                a1.append(x)
8            else:
9                a2.append(x)
10        return a1 + a2