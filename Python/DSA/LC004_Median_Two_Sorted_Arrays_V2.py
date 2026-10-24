class Solution:
    def findMedianSortedArrays(
        self, nums1: list[int], nums2: list[int]
    ) -> float:
        # Combine both arrays into one
        nums = nums1 + nums2

        # Sort the combined array
        nums.sort()

        # Find the middle index
        mid = len(nums) // 2

        # If length is odd, return the middle element
        if len(nums) % 2 != 0:
            result = nums[mid]
        else:
            # If length is even, average the two middle elements
            result = (nums[mid] + nums[mid - 1]) / 2

        return result
      
