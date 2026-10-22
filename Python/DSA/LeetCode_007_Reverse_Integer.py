class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2147483648, 2147483647

        res = 0
        negative = x < 0
        x = abs(x)

        # Reverse digits while checking the integer limit
        limit = INT_MAX if not negative else abs(INT_MIN)

        while x != 0:
            digit = x % 10
            x //= 10

            if res > (limit - digit) // 10:
                return 0

            res = res * 10 + digit

        return -res if negative else res
      
