class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            # Calculate the sum on the right
            if left_sum == total_sum - left_sum - num:
                return i

            left_sum += num

        return -1
