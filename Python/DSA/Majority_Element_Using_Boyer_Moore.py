class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            # Increase count for candidate, otherwise decrease it
            count += 1 if num == candidate else -1

        return candidate
