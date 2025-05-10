
# sub arrays of two elements each

arr = [1,2,3,4]
arr2 = []
i = 0
while i < len(arr):
    j = i+1
    while j < len(arr):
        arr2.append((arr[i],arr[j]))
        j += 1
    i += 1
    
print(arr2)

 
arr = [1,2,3,4]
n = len(arr)
arr2 = [(arr[i],arr[j]) for i in range(n) for j in range(i+1,n)]
print(arr2)

arr = [1,2,3,4]

n = len(arr)
arr2 = [(arr[i],arr[j],arr[k]) for i in range(n) for j in range(i+1,n) for k in range(j+1,n)]
print(arr2)
 