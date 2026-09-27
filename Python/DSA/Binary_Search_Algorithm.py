def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        # Search in the right half
        elif arr[mid] < target:
            left = mid + 1

        # Search in the left half
        else:
            right = mid - 1

    return -1


numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

target = 23

result = binary_search(numbers, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found")
