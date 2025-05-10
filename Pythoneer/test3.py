
arr = [4,6,7,8,9,9,9,10,10,15]

arr.sort(reverse = True)

print(arr)

sranks = list(range(1,len(arr)+1))

i = 1

while i < len(arr):
    if arr[i-1] == arr[i]:
        sranks[i] = sranks[i-1]
        
    i += 1
    

print(sranks)
