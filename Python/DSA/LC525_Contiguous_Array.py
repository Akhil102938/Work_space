class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        balance = 0
        max_length = 0

        # Store the earliest index for each balance
        first_seen = {0: -1}

        for i, num in enumerate(nums):
            # Treat 0 as -1 and 1 as +1
            if num == 0:
                balance -= 1
            else:
                balance += 1

            # A repeated balance means the subarray has equal 0s and 1s
            if balance in first_seen:
                length = i - first_seen[balance]
                max_length = max(max_length, length)
            else:
                # Keep the earliest index for this balance
                first_seen[balance] = i

        return max_length
      
