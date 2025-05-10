'''Find the greatest number that will divide 45, 91 and 183 as to 
    leave the same remainder in each case 
    for the given numbers answer is 46'''


def getFactors(n):
    factors = []
    for i in range(1,n+1):
        if n%i == 0:
            factors.append(i)
    return factors

def solve(arr2):
    arr = []
    for i in range(len(arr2)):
        for j in range(i+1,len(arr2)):
            arr.append(abs(arr2[i]-arr2[j]))
    
    cf = []
    for i in arr:
        cf.append(set(getFactors(i))) 
        
    ist = lambda x,y: x.intersection(y)
    one = cf[0]
    for i in cf:
        one = ist(one,i)
  
    hcf = max(one)
    return hcf 
    
  
arr = [45,91,183]
print(solve(arr))


