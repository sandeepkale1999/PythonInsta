
def getFactors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors


    
arr = [16,32,64,128]
cf = []
for i in arr:
    cf.append(set(getFactors(i))) 
        
print(cf)

ist = lambda x,y: x.intersection(y)
one = cf[0]
for i in cf:
    one = ist(one,i)

    
print('common factors',one)
print('highest common factor',max(one))
    
