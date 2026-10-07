class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)

        # Sum of numbers from 0 to n
        expected_sum = n * (n + 1) // 2

        # Difference gives the missing number
        return expected_sum - sum(nums)
