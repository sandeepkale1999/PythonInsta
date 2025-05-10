# python program to get all possible arrays which can be made up of given array
# important concept while solving problems


from itertools import combinations

arr = [1,2,3]    # op [1],[1,2],[1,2,3],[2,3],[1,3]

allArrays = list()

print(list(combinations(arr,1)))
print(list(combinations(arr,2)))
print(list(combinations(arr,3)))

for i in range(1,len(arr)+1):
    allArrays.extend(list(combinations(arr,i)))
    
print(allArrays)


def getAllArrays(arr):
    allArrays = []
    for i in range(1, len(arr)):
        allArrays.extend([list(i) for i in list(combinations(arr,i))])
        
    print(allArrays)
    
arr2 = [1,2,3,4]
getAllArrays(arr2)


## other utility..
# given an array and make all possible sub arrays which will contain only three elements

arr = [1,2,3,4]

res = list(combinations(arr,3))
print(res)

res2 = [list(tup) for tup in list(combinations(arr,3))]
print(res2)
