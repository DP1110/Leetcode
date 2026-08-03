class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Pruning: smallest possible sum with nums[i]
            min_sum = nums[i] + nums[i + 1] + nums[i + 2]
            if min_sum >= target:
                if abs(min_sum - target) < abs(closest_sum - target):
                    closest_sum = min_sum
                if min_sum == target:
                    return target
                break  # Larger i will only increase the sum
            
            # Pruning: largest possible sum with nums[i]
            max_sum = nums[i] + nums[n - 2] + nums[n - 1]
            if max_sum <= target:
                if abs(max_sum - target) < abs(closest_sum - target):
                    closest_sum = max_sum
                if max_sum == target:
                    return target
                continue  # Need larger nums[i] to get closer
            
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                if current_sum == target:
                    return current_sum
                
                if current_sum < target:
                    left += 1
                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return closest_sum