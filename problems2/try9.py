

arr = [16,3,15,10,16,17,16,1]

one = []
two = []
 
i = 0
while i <len(arr):
    if i%2 == 0:
        one.append(arr[i])
    else:
        two.append(arr[i])
    i += 1
    
    x = 0
    c = 0
    for y in range(1,len(one)):
        if one[x] != one[y]:
            c += 1
            x += 1
    z = 0
    for w in range(1,len(two)):
        if two[z] != two[w]:
            c += 1
            z += 1
    
print(c)        
 