
from itertools import combinations
strr = '423'

arr = []
for i in range(1,len(strr)+1):
    arr += list(combinations(strr,i))
    
                   
    
print(arr)

s = 0
arr2 = []
for t in arr:
    s += int(''.join(t))
    arr2.append(int(''.join(t)))
    
print(s)
print(arr2)
#print(''.join(('a','b')))
    