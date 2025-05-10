# prime number program
import math
def isPrime(n):
    if n > 1:
        if n == 2:
            return True
        else:
            for i in range(2,int(math.sqrt(n))+1,2):
                if n%i == 0:
                    return False
            else:
                return True 
        


def isPrime2(n):
    if n>1:
        if n == 0:
            return True
        else:
            for i in range(2,int(n**0.5)+1,2):
                if n%i == 0:
                    return False
            else:
                return True
            
print(isPrime2(11))

