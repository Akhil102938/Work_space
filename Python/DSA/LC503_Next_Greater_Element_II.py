from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1] * n
        stack = []

        # Traverse the circular array twice
        for i in range(2 * n - 1, -1, -1):
            current = nums[i % n]

            # Remove elements that are smaller than or equal to current
            while stack and nums[stack[-1]] <= current:
                stack.pop()

            # Record answers only during the original array's pass
            if i < n and stack:
                answer[i] = nums[stack[-1]]

            # Store the current element's index
            stack.append(i % n)

        return answer
      
