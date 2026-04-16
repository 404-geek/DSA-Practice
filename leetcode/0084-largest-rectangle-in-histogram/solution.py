class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        max_area = 0

        stack = []

        for i in range(n):

            while stack and heights[i] < heights[stack[-1]]:

                h = heights[stack.pop()]
                left_smaller = stack[-1] if stack else -1
                w = i - left_smaller - 1
                max_area = max(max_area, h * w)

            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            left_smaller = stack[-1] if stack else -1
            w = n - left_smaller - 1
            max_area = max(max_area, h * w)

        return max_area
