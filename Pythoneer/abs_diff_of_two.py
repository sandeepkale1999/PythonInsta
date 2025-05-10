         
        
# understand the difference in follwing three        
        
from itertools import permutations, combinations
print(list(permutations(arr,2)))
twos = [(arr[i], arr[j]) for i in range(len(arr)) for j in range(i+1,len(arr))]
print(twos)
print(list(combinations(arr,2)))