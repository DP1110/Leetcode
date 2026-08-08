1class Solution:
2    def canJump(self, nums):
3        reach = 0
4        for i, n in enumerate(nums):
5            if i > reach:
6                return False
7            reach = max(reach, i + n)
8        return True