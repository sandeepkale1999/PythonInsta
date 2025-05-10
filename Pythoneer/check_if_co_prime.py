# two numbers are coprine if their hcf is 1 
def isCoprime(a,b):
    fact1 = []
    fact2 = []
    for i in range(1, a+1):
        if a%i == 0:
            fact1.append(i)
    for j in range(1, b+1):
        if b%j == 0:
            fact2.append(j)
            
    #print(fact1,fact2)
    #print(set(fact1).intersection(set(fact2)))
    if set(fact1).intersection(set(fact2)) == {1}:
        return True
    else:
        return False
    
            
#print(isCoprime(18,35))

 