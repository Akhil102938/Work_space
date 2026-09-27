def longest_consecutive(arr):
    nums = set(arr)
    longest = 0

    for x in nums:
        # Start of a sequence
        if x - 1 not in nums:
            current = x
            length = 1

            # Find consecutive numbers
            while current + 1 in nums:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [100, 4, 200, 1, 3, 2]

print(longest_consecutive(arr))
