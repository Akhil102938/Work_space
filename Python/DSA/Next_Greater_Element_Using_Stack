def next_greater(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        current = nums[i]

        # Find greater element for previous values
        while stack and nums[stack[-1]] < current:
            index = stack.pop()
            result[index] = current

        stack.append(i)

    return result


nums = [3, 1, 5, 2, 4]

print(next_greater(nums))
