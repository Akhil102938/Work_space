class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Store unique characters in the current window
        char_set = set()
        left = 0
        max_length = 0

        # Expand the window by moving the right pointer
        for right in range(len(s)):

            # Shrink the window until the duplicate is removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the window
            char_set.add(s[right])

            # Update the longest valid window length
            max_length = max(max_length, right - left + 1)

        return max_length
      
