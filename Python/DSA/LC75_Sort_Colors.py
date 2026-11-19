from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:

        # Initialize three pointers
        low, mid, high = 0, 0, len(nums) - 1

        # Process elements until the pointers cross
        while mid <= high:

            if nums[mid] == 0:
                # Move 0 to the beginning
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                # Keep 1 in the middle
                mid += 1

            else:
                # Move 2 to the end
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

                # Don't increment mid because the swapped value
                # still needs to be checked
              
