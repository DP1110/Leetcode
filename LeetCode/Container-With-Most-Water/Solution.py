1class Solution(object):
2    def maxArea(self, height):
3        left, right = 0, len(height) - 1
4        max_area = 0
5        
6        while left < right:
7            # Width between the two lines
8            width = right - left
9            # Height is limited by the shorter line
10            h = min(height[left], height[right])
11            # Calculate area
12            area = width * h
13            max_area = max(max_area, area)
14            
15            # Move the pointer with the shorter line inward
16            if height[left] < height[right]:
17                left += 1
18            else:
19                right -= 1
20        
21        return max_area