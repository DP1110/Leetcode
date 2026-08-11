class Solution:
    def largestRectangleArea(self, heights):
        stack = []  # stores indices, heights are increasing
        max_area = 0
        n = len(heights)
        
        for i in range(n + 1):
            # Use 0 as sentinel to flush remaining bars
            curr_height = heights[i] if i < n else 0
            
            while stack and curr_height < heights[stack[-1]]:
                height = heights[stack.pop()]
                # If stack is empty after pop, width extends from index 0 to i-1
                # Otherwise, width extends from stack[-1]+1 to i-1
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            
            stack.append(i)
        
        return max_area