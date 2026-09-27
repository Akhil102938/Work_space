nums = [10, 20, 30, 40, 50, 30]

# Remove duplicates using set
set1 = set(nums)

print(set1)

# Compare original and unique lengths
if len(nums) != len(set1):
    print("Duplicate exists")
