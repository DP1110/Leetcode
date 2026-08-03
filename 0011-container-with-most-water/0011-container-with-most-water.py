class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # Width between the two lines
            width = right - left
            # Height is limited by the shorter line
            h = min(height[left], height[right])
            # Calculate area
            area = width * h
            max_area = max(max_area, area)
            
            # Move the pointer with the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area