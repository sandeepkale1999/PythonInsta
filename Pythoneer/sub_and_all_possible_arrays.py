# all possible subarrays
arr = [1,2,3]  # op [[1],[2],[3],[1,2],[2,3],[1,2,3]]

arr2 = []
c = 0
while c < len(arr):
    i = 0
    j = 1 + c
    while j <= len(arr):
        arr2.append(arr[i:j])
        i += 1
        j += 1
    c += 1
    
    
print(arr2)

# all possible arrays
arr = [1,2,3]  #op [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
from itertools import combinations
arr3 = []
for i in range(1,len(arr)+1):
    arr3 += map(list,list(combinations(arr,i)))
    
print(arr3)
