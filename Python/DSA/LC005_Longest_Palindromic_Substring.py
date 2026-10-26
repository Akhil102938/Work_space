class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start = end = 0

        for i in range(len(s)):
            # Check odd-length palindrome
            len1 = self._expand(s, i, i)

            # Check even-length palindrome
            len2 = self._expand(s, i, i + 1)

            max_len = max(len1, len2)

            # Update the longest palindrome boundaries
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

    def _expand(self, s: str, left: int, right: int) -> int:
        # Expand while the characters match
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
      
