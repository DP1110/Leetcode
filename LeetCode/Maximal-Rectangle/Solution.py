1class Solution:
2    def maximalRectangle(self, matrix):
3        if not matrix or not matrix[0]:
4            return 0
5        
6        rows = len(matrix)
7        cols = len(matrix[0])
8        heights = [0] * cols
9        max_area = 0
10        
11        for r in range(rows):
12            # Update histogram heights for this row
13            for c in range(cols):
14                if matrix[r][c] == '1':
15                    heights[c] += 1
16                else:
17                    heights[c] = 0
18            
19            # Find largest rectangle in this histogram
20            max_area = max(max_area, self.largestRectangleArea(heights))
21        
22        return max_area
23    
24    def largestRectangleArea(self, heights):
25        stack = []
26        n = len(heights)
27        max_area = 0
28        
29        for i in range(n + 1):
30            curr_height = heights[i] if i < n else 0
31            
32            while stack and curr_height < heights[stack[-1]]:
33                height = heights[stack.pop()]
34                width = i if not stack else i - stack[-1] - 1
35                max_area = max(max_area, height * width)
36            
37            stack.append(i)
38        
39        return max_area