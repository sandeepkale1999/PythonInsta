
arr = [6,2,4,10]


twos = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        t = sorted((arr[i],arr[j]))
        if t not in twos:
            twos.append(t)
        
print(twos)
        
difs = []
for j in twos:
    difs.append(abs(j[0]-j[1]))

for t in sorted(twos):
    if abs(t[0]-t[1]) == min(difs):
        print(t)
        
        
        
        
        
        
        
from itertools import permutations, combinations
print(list(permutations(arr,2)))
twos = [(arr[i], arr[j]) for i in range(len(arr)) for j in range(i+1,len(arr))]
print(twos)
print(list(combinations(arr,2)))