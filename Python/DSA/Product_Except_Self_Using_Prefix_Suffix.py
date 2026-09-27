def product_except_self(nums):
    n = len(nums)
    answer = [1] * n

    # Store left products
    left = 1
Product_Except_Self_Using_Prefix_Suffix
    for i in range(n):
        answer[i] = left
        left *= nums[i]

    # Multiply by right products
    right = 1

    for i in range(n - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer


nums = [1, 2, 3, 0, 4]

result = product_except_self(nums)

print(result)
