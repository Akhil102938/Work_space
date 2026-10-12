
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)

        # Check whether a prefix length is common to all strings
        def is_common_prefix(length: int) -> bool:
            prefix = strs[0][:length]
            return all(s.startswith(prefix) for s in strs)

        low, high = 0, min_len
        longest_prefix = ""

        # Binary search for the longest common prefix
        while low <= high:
            mid = (low + high) // 2

            if is_common_prefix(mid):
                longest_prefix = strs[0][:mid]
                low = mid + 1
            else:
                high = mid - 1

        return longest_prefix
      
