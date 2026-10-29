from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Maximum money two houses back
        prev2 = 0

        # Maximum money from the previous house
        prev1 = 0

        # Process each house
        for i in range(len(nums)):
            # Choose between robbing this house or skipping it
            current = max(nums[i] + prev2, prev1)

            # Update values for the next iteration
            prev2 = prev1
            prev1 = current

        # Return the maximum money that can be robbed
        return prev1
      
