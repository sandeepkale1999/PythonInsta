'''deloitte problem'''

def is_prime(num):
    if num == 2:
        return True 
    else:
        for i in range(2,num):
            if num%i == 0:
                return False
                
        else:
            return True
           
num = 2
num2 = num
num3 = num

prime1 = []
prime2 = []

while len(prime1) < 7:
    if is_prime(num2):
        prime1.append(num2)
    num2 += 1
    
while len(prime2) < 7 and num3 >= 2:
    if is_prime(num3):
        prime2.append(num3)
    num3 -= 1
    
prime1.sort()
prime2.sort()

print(prime1)
print(prime2)
primes = prime2+prime1
print(primes)

diff = [abs(num-i) for i in primes]
print(diff)

for j in primes:
    if abs(j-num) == max(diff):
        primes.remove(j)
       
        
print(primes)
diff.remove(max(diff))

final = []
for k in primes:
    if abs(k-num) == max(diff):
        final.append(k)
        
print(min(final))


