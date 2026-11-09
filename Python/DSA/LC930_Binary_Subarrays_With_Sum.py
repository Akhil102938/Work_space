class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        # Counts subarrays whose sum is at most the given goal
        def atMost(goal: int) -> int:
            if goal < 0:
                return 0

            total_count = 0
            current_sum = 0
            left = 0

            for right in range(len(nums)):
                # Expand the window
                current_sum += nums[right]

                # Shrink the window if sum exceeds goal
                while current_sum > goal:
                    current_sum -= nums[left]
                    left += 1

                # Count all valid subarrays ending at right
                total_count += right - left + 1

            return total_count

        # Exactly goal = AtMost(goal) - AtMost(goal - 1)
        return atMost(goal) - atMost(goal - 1)
      
