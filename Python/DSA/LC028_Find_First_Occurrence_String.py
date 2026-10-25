class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        # Check every possible starting position
        for i in range(n - m + 1):
            # Compare the substring with needle
            if haystack[i:i + m] == needle:
                return i

        # Return -1 if needle is not found
        return -1
      
