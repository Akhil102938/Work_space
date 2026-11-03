class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Handle an empty list
        if not nums:
            return 0

        # Sort the numbers to place consecutive values together
        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):
            # Ignore duplicate values
            if nums[i] == nums[i - 1]:
                continue

            # Extend the current sequence
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                # Update the longest sequence and start a new one
                longest = max(longest, current)
                current = 1

        # Include the final sequence in the result
        return max(longest, current)
