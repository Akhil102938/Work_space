arr = [2, 1, 5, 1, 3, 2]
k = 7

left = 0
current_sum = 0
max_length = 0

for right in range(len(arr)):
    current_sum += arr[right]

    # Shrink window if sum exceeds k
    while current_sum > k:
        current_sum -= arr[left]
        left += 1

    max_length = max(max_length, right - left + 1)

print("Max. length:", max_length)
