class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height_index = stack.pop()
                height = heights[height_index]

                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        n = len(heights)

        while stack:
            height_index = stack.pop()
            height = heights[height_index]

            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)

        return max_area
