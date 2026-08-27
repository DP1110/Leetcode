1class Solution(object):
2    def findDuplicate(self, nums):
3        slow = fast = nums[0]
4        while True:
5            slow = nums[slow]
6            fast = nums[nums[fast]]
7            if slow == fast:
8                break
9        slow = nums[0]
10        while slow != fast:
11            slow = nums[slow]
12            fast = nums[fast]
13        return slow