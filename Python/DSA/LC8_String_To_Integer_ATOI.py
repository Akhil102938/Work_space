class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove leading whitespace
        s = s.lstrip()

        if not s:
            return 0

        # Determine the sign
        sign = 1
        i = 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        res = 0

        # Convert consecutive digits into an integer
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        res *= sign

        # Define 32-bit signed integer limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Clamp the result within the allowed range
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX

        return res
      
