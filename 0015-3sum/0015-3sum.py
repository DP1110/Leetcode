class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early termination: if nums[i] > 0, sum can't be 0
            if nums[i] > 0:
                break
            
            left, right = i + 1, n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # Need a larger sum
                
                else:
                    right -= 1  # Need a smaller sum
        
        return result