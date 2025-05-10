import math
def isPrime(n):
    if n > 1:
        if n == 2:
            return True
        for i in range(2,int(math.sqrt(n))):
            if n%i == 0:
                return False
            
        else:
            return True
        
        
print(isPrime(12))
print(isPrime(11))
print(isPrime(1))