1class Solution:
2    def threeSumClosest(self, nums, target):
3        nums.sort()
4        n = len(nums)
5        closest_sum = float('inf')
6        
7        for i in range(n - 2):
8            # Skip duplicate values for the first element
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11            
12            # Pruning: smallest possible sum with nums[i]
13            min_sum = nums[i] + nums[i + 1] + nums[i + 2]
14            if min_sum >= target:
15                if abs(min_sum - target) < abs(closest_sum - target):
16                    closest_sum = min_sum
17                if min_sum == target:
18                    return target
19                break  # Larger i will only increase the sum
20            
21            # Pruning: largest possible sum with nums[i]
22            max_sum = nums[i] + nums[n - 2] + nums[n - 1]
23            if max_sum <= target:
24                if abs(max_sum - target) < abs(closest_sum - target):
25                    closest_sum = max_sum
26                if max_sum == target:
27                    return target
28                continue  # Need larger nums[i] to get closer
29            
30            left, right = i + 1, n - 1
31            
32            while left < right:
33                current_sum = nums[i] + nums[left] + nums[right]
34                
35                if abs(current_sum - target) < abs(closest_sum - target):
36                    closest_sum = current_sum
37                
38                if current_sum == target:
39                    return current_sum
40                
41                if current_sum < target:
42                    left += 1
43                    # Skip duplicate left values
44                    while left < right and nums[left] == nums[left - 1]:
45                        left += 1
46                else:
47                    right -= 1
48                    # Skip duplicate right values
49                    while left < right and nums[right] == nums[right + 1]:
50                        right -= 1
51        
52        return closest_sum