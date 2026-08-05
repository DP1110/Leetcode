1class Solution:
2    def search(self, nums, target):
3        left, right = 0, len(nums) - 1
4        
5        while left <= right:
6            mid = (left + right) // 2
7            
8            if nums[mid] == target:
9                return mid
10            
11            # Left half is sorted
12            if nums[left] <= nums[mid]:
13                if nums[left] <= target < nums[mid]:
14                    right = mid - 1
15                else:
16                    left = mid + 1
17            # Right half is sorted
18            else:
19                if nums[mid] < target <= nums[right]:
20                    left = mid + 1
21                else:
22                    right = mid - 1
23        
24        return -1