1class Solution:
2    def searchRange(self, nums, target):
3        def findLeft():
4            left, right = 0, len(nums) - 1
5            index = -1
6            while left <= right:
7                mid = (left + right) // 2
8                if nums[mid] == target:
9                    index = mid
10                    right = mid - 1  # Keep searching left
11                elif nums[mid] < target:
12                    left = mid + 1
13                else:
14                    right = mid - 1
15            return index
16        
17        def findRight():
18            left, right = 0, len(nums) - 1
19            index = -1
20            while left <= right:
21                mid = (left + right) // 2
22                if nums[mid] == target:
23                    index = mid
24                    left = mid + 1   # Keep searching right
25                elif nums[mid] < target:
26                    left = mid + 1
27                else:
28                    right = mid - 1
29            return index
30        
31        return [findLeft(), findRight()]