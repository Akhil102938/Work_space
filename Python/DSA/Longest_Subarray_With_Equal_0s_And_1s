def find_max_length(arr):
    prefix_sum = 0
    max_len = 0

    # prefix_sum : first index where it appeared
    seen = {0: -1}

    for i in range(len(arr)):

        # Convert 0 → -1
        if arr[i] == 0:
            prefix_sum -= 1
        else:
            prefix_sum += 1

        # Have we seen this balance before?
        if prefix_sum in seen:
            length = i - seen[prefix_sum]
            max_len = max(max_len, length)
        else:
            # Store ONLY the first occurrence
            seen[prefix_sum] = i

    return max_len


arr = [0, 1, 0, 1, 1, 1, 0]

print(find_max_length(arr))
