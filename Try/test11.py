from itertools import combinations

arr = [1,2,3]

arr2 = [(arr[i], arr[j], arr[k]) for i in range(len(arr)) for j in range(i, len(arr)) for k in range(j, len(arr))]
print(arr2)

arr = [1,2,3,4]
arr3 = list(combinations(arr,3))
print(arr3)