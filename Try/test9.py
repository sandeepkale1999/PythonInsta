def rshift(arr,n):
    for i in range(n):
        arr.append(arr.pop(0))
    print(arr)
    

def lshift(arr,n):
    for i in range(n):
        arr.insert(0,arr.pop())
    print(arr)
    print(arr[0])
    return arr[0]


inp = '56237'
n = 3
arr = list(inp)
print(arr) 
res = ''
for i in inp:
    if int(i)%2 != 0:
        res += str(lshift(arr,n))
    else:
        res += i
        
print(res)
                   