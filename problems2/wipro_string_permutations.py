## find all permutations of a string

from itertools import permutations


def allPermutations(str):
    arr = []
    permList = permutations(str)
    
    for perms in list(permList):
        arr.append(''.join(perms))

    return arr


num = '734'
arr = allPermutations(num)
arr = list(map(int,arr))
arr.sort
print(arr)
 
print(min(arr)+max(arr))