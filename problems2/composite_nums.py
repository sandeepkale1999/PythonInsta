#  How many composite numbers in a given range. 

# prime checker 
def prime(n):
    if n>1:
        if n==2:
            return True
        else:
            for i in range(2,int(n**0.5)+1,2):
                if n%i == 0:
                    return False
            else:
                return True
  
n = 10
c = 0
for i in range(1,n+1):
    if not prime(i) or i == 2:
        c += 1
        
print(c)
n = 10
c = 0 
for i in range(1,n+1):
    if i == 2:
        c += 1
    else:
        for j in range(2,i):
            if i%j == 0:
                c += 1
                break 
    
print(c)




