class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        freq = {}

        # Count the frequency of each number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Check whether any number appears more than once
        for num in freq:
            if freq[num] > 1:
                return True

        return False
