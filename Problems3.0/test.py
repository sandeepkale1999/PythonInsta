def isPrime(n):
    if n > 1:
        if n == 2:
            return True
        else:
            for i in range(2, int(n**0.5), 2):
                if n%i == 0:
                    return False
            return True
        
   
n = int(input())
arr = list(range(1,n+1))
print(arr)
c = 0
while len(arr) != 1:
    d = 0
    for i in arr:
        if isPrime(i):
            arr.remove(i)
            d += 1
    c += 1
    arr = list(range(1,len(arr)+1))
    
print(c)