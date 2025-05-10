def isPrime(n):
    if n > 1:
        if n == 2:
            return True
        if n%2 == 0:
            return False
        else:
            for i in range(2, n//2):
                if n%i == 0:
                    return False
            return True
        
   
n = int(input())
arr = list(range(1,n+1))
c = 1
while len(arr) != 1:
    d = 0
    arr2 = arr.copy()
    for i in arr2:
        if isPrime(i):
            arr.remove(i)
            d += 1
    c += 1
    arr = list(range(1,len(arr)+1))
print(c)
