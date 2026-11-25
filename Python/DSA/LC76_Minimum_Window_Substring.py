from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)
        window = Counter()

        required = len(need)
        formed = 0

        left = 0
        min_len = float("inf")
        min_start = 0

        for right, ch in enumerate(s):
            window[ch] += 1

            # Check whether this character requirement is satisfied
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Shrink while all requirements are satisfied
            while left <= right and formed == required:
                current_len = right - left + 1

                if current_len < min_len:
                    min_len = current_len
                    min_start = left

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        return "" if min_len == float("inf") else s[min_start:min_start + min_len]
      
