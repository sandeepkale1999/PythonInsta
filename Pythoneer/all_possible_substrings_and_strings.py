# all possible substrings inp 'san' op ['s', 'a', 'n', 'sa', 'an', 'san']

name = 'san'

n = len(name)

subStr = []
c = 0
while c <= n:
    i = 0
    j = c+1
    while j <= n:
        subStr.append(name[i:j])
        i += 1
        j += 1
    c += 1
    
print(subStr)

# all possible strings made from given string

from itertools import combinations, permutations
name = 'san'
allStrs = []
for i in range(1, len(name)+1):
    for j in list(combinations(name,i)):
        for k in list(permutations(j)):
            newStr = ''.join(k)
            if newStr not in allStrs:
                allStrs.append(newStr)
        
    
print(allStrs)



