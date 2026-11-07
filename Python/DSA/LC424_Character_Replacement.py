class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Store the frequency of characters in the window
        count = {}

        left = 0
        max_freq = 0
        max_len = 0

        # Expand the sliding window
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            # Track the highest character frequency
            max_freq = max(max_freq, count[s[right]])

            # Check whether replacements exceed k
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update the longest valid window
            max_len = max(max_len, right - left + 1)

        return max_len
      
