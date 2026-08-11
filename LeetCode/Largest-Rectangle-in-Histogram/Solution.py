1class Solution:
2    def largestRectangleArea(self, heights):
3        stack = []  # stores indices, heights are increasing
4        max_area = 0
5        n = len(heights)
6        
7        for i in range(n + 1):
8            # Use 0 as sentinel to flush remaining bars
9            curr_height = heights[i] if i < n else 0
10            
11            while stack and curr_height < heights[stack[-1]]:
12                height = heights[stack.pop()]
13                # If stack is empty after pop, width extends from index 0 to i-1
14                # Otherwise, width extends from stack[-1]+1 to i-1
15                width = i if not stack else i - stack[-1] - 1
16                max_area = max(max_area, height * width)
17            
18            stack.append(i)
19        
20        return max_area