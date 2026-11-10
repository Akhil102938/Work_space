from collections import deque

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_deque = deque()  # Maintains elements in decreasing order
        min_deque = deque()  # Maintains elements in increasing order

        left = 0
        ans = 0

        for right, val in enumerate(nums):

            # Remove smaller elements from the maximum deque
            while max_deque and max_deque[-1] < val:
                max_deque.pop()
            max_deque.append(val)

            # Remove larger elements from the minimum deque
            while min_deque and min_deque[-1] > val:
                min_deque.pop()
            min_deque.append(val)

            # Shrink window while max - min exceeds the limit
            while max_deque[0] - min_deque[0] > limit:

                # Remove outgoing element if it is at the front
                if max_deque[0] == nums[left]:
                    max_deque.popleft()

                if min_deque[0] == nums[left]:
                    min_deque.popleft()

                left += 1

            # Update the maximum valid window length
            ans = max(ans, right - left + 1)

        return ans
      
