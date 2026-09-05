a = [1, 1, 2, 2, 2, 3, 4, 4, 5]
j=0
for i in range(1,len(a)):
    if a[i] != a[j]:
          j += 1
          a[j] = a[i]
        
print("Before :",a)

for i in range(0,j + 1):
    print("After :",a[i])
