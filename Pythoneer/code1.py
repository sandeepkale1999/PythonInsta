
arr = [1,2,3]

arr2 = []

for i in range(len(arr)):
    for j in range(i,len(arr)):
        for k in range(j,len(arr)):
            arr2.append((arr[i],arr[j],arr[k]))
            
            
print(arr2)
