class Solution:
    def searchRange(self, nums, target):
        def findLeft():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1  # Keep searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        
        def findRight():
            left, right = 0, len(nums) - 1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1   # Keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        
        return [findLeft(), findRight()]