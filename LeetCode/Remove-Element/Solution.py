1class Solution:
2    def removeElement(self, nums, val):
3        k = 0
4        
5        for num in nums:
6            if num != val:
7                nums[k] = num
8                k += 1
9        
10        return k