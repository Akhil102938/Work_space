class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Start with the widest possible container
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area using the shorter boundary
            current_area = min(height[left], height[right]) * (right - left)

            # Keep track of the maximum area found
            max_area = max(max_area, current_area)

            # Move the pointer at the shorter boundary
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
      
