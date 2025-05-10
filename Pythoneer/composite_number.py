import math
def isComposite(n):
    if n > 1:
        for i in range(2,int(math.sqrt(n))):
            if n%i == 0:
                return True
        else:
            return False
            
    
print(isComposite(2))
print(isComposite(12))
print(isComposite(11))