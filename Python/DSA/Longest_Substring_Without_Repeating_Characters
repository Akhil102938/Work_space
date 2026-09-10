def length_of_longest_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Remove characters until duplicate is gone
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


s = "abcabcbb"

result = length_of_longest_substring(s)

print("Longest substring length:", result)
