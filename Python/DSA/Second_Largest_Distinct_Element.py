class Solution:
    def secondLargest(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return None

        first = second = float('-inf')

        for num in nums:
            if num > first:
                second = first
                first = num

            elif first > num > second:
                second = num

        # No second distinct element
        return second if second != float('-inf') else None
