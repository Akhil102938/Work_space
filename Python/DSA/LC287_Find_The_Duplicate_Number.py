class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        # Initialize slow and fast pointers
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find the meeting point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find the entrance of the cycle
        ptr1 = nums[0]
        ptr2 = slow

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        # The cycle entrance is the duplicate number
        return ptr1
      
