arr = [1, 2, 3, 4, 6, 8, 11]
target = 10

left = 0
right = len(arr) - 1

while left < right:
    total = arr[left] + arr[right]

    if total == target:
        print("Found", arr[left], arr[right])
        break

    # Move pointers based on the sum
    elif total < target:
        left += 1
    else:
        right -= 1
