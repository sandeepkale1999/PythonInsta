
def isPrime(n):
    if n > 1:
        if n == 2:
            return True
        else:
            for i in range(2, int(n**0.5), 2):
                if n%i == 0:
                    return False
            return True
        
    

def getNum(arr):
    
    rem = arr.pop(arr.index(min(arr)))
    num = max(arr)

    if rem%2 == 0:
        for i in arr:
            if i % 2 == 0:
                return None
    else:
        while True:
            if isPrime(num):
                c = 0
                for i in arr:
                    if num%i == rem:
                        c += 1
                        
                if c == len(arr):
                    return num
            num += 1
    
arr = [3,4,5,1]

print(getNum(arr))


'''    
PRIME CONSTRUCTION CODE

from math import gcd
l=list(map(int,input().split()))
q=min(l)
lcm=1
for i in l:
  lcm=lcm*i//gcd(lcm,i)
r=lcm+q
a=2
while r>a:
    if r%a==0 & a!=r:
      print("None",end="")
      a=a+1
      break;
    else:
      print(r,end="")
      a=(r)+1'''