from itertools import combinations, permutations 
num = 123  # 1,2,3,12,23,13,123,21,32,31,321,312
snum = str(num)
print(list(combinations(str(num),1)))

print(list(permutations(str(num))))

arr = []

for i in range(1,len(snum)+1):
    for k in list(combinations(snum,i)):
        for j in permutations(k):
            arr.append(int(''.join(j)))
            
print(arr)

def getAllCombns(itr):
    if type(itr) == int:
        strr = str(itr)
    else:
        strr = itr
    
    arr = []
    for i in range(1,len(strr)+1):
        for j in list(combinations(strr,i)):
            for k in permutations(j):
                try:
                    arr.append(int(''.join(k)))
                except Exception:
                    arr.append(''.join(k))
                    
    return arr


num = 123
print(getAllCombns(num))
strr = 'abc'
print(getAllCombns(strr))


