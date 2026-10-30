class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []

        # Sort the array to use two pointers
        nums.sort()

        for i, a in enumerate(nums):

            # Skip duplicate first elements
            if i > 0 and a == nums[i - 1]:
                continue

            # Initialize two pointers
            l, r = i + 1, len(nums) - 1

            while l < r:
                # Calculate the sum of three numbers
                total = a + nums[l] + nums[r]

                if total > 0:
                    # Sum is too large, move right pointer left
                    r -= 1

                elif total < 0:
                    # Sum is too small, move left pointer right
                    l += 1

                else:
                    # Found a valid triplet
                    res.append([a, nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # Skip duplicate left values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip duplicate right values
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return res
