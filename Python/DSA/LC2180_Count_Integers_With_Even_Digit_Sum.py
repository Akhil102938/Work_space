class Solution:
    def countEven(self, num: int) -> int:
        ans = 0

        # Check every integer from 1 through num
        for i in range(1, num + 1):

            # Calculate the sum of the digits
            digit_sum = sum(int(c) for c in str(i))

            # Count integers whose digit sum is even
            if digit_sum % 2 == 0:
                ans += 1

        return ans
      
