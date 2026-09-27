arr = [1, 2, 3, 4]
pro = 1

# Calculate total product
for i in range(len(arr)):
    pro *= arr[i]

# Divide by each element
for i in range(len(arr)):
    print(pro / arr[i])
