1class Solution(object):
2    def threeSum(self, nums):
3        nums.sort()
4        n = len(nums)
5        result = []
6        
7        for i in range(n - 2):
8            # Skip duplicate values for the first element
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11            
12            # Early termination: if nums[i] > 0, sum can't be 0
13            if nums[i] > 0:
14                break
15            
16            left, right = i + 1, n - 1
17            
18            while left < right:
19                total = nums[i] + nums[left] + nums[right]
20                
21                if total == 0:
22                    result.append([nums[i], nums[left], nums[right]])
23                    
24                    # Skip duplicates for left and right
25                    while left < right and nums[left] == nums[left + 1]:
26                        left += 1
27                    while left < right and nums[right] == nums[right - 1]:
28                        right -= 1
29                    
30                    left += 1
31                    right -= 1
32                
33                elif total < 0:
34                    left += 1  # Need a larger sum
35                
36                else:
37                    right -= 1  # Need a smaller sum
38        
39        return result