class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Dutch National Flag: three pointers
        # [0, left)   -> 0s
        # [left, mid) -> 1s
        # (right, n-1] -> 2s
        # [mid, right] -> unknown
        
        left, mid, right = 0, 0, len(nums) - 1
        
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1