1class Solution:
2    def fourSum(self, nums, target):
3        nums.sort()
4        n = len(nums)
5        result = []
6        
7        for i in range(n - 3):
8            # Skip duplicate first elements
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11            
12            # Pruning: smallest possible sum with nums[i] is already too large
13            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
14                break
15            
16            # Pruning: largest possible sum with nums[i] is still too small
17            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
18                continue
19            
20            for j in range(i + 1, n - 2):
21                # Skip duplicate second elements
22                if j > i + 1 and nums[j] == nums[j - 1]:
23                    continue
24                
25                # Pruning for j
26                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
27                    break
28                
29                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
30                    continue
31                
32                left, right = j + 1, n - 1
33                
34                while left < right:
35                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
36                    
37                    if current_sum == target:
38                        result.append([nums[i], nums[j], nums[left], nums[right]])
39                        
40                        # Skip duplicates for third element
41                        while left < right and nums[left] == nums[left + 1]:
42                            left += 1
43                        # Skip duplicates for fourth element
44                        while left < right and nums[right] == nums[right - 1]:
45                            right -= 1
46                        
47                        left += 1
48                        right -= 1
49                    
50                    elif current_sum < target:
51                        left += 1
52                    else:
53                        right -= 1
54        
55        return result