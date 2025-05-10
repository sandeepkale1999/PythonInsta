 
n = int(input())
arr = [int(x) for x in input().split()]
(p,x,z) = map(int, input().split()) 
 
final = []
for i in range(len(arr)):
    if arr[i]%x == z:
        final.append(arr[i])
        
final.sort()
print(arr.index(final[p-1]))


