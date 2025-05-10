# find all permutaions for a given string

from itertools import permutations

strr = 'hey'
permList = permutations(strr)

for perm in list(permList):
    print(''.join(perm), end = ' ')
    
print()    
    
arr = [1,2,3]
print(list(permutations(arr)))