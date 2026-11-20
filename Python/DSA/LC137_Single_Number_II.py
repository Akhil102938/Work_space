class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Track bits appearing once and twice
        ones = 0
        twos = 0

        for num in nums:
            # Update bits that have appeared once
            ones = (ones ^ num) & ~twos

            # Update bits that have appeared twice
            twos = (twos ^ num) & ~ones

        # Return the number appearing only once
        return ones
      
