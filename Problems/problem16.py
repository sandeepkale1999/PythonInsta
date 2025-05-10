import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False
 
    max_div = math.floor(math.sqrt(n))
    for i in range(3, 1 + max_div, 2):
        if n % i == 0:
            return False
    return True
    
    
            
(start, des) = map(int, input().split())
start = start + 1
count = 1
final = 0
while count <=des:
    if is_prime(start):
        count += 1
        final = start 
    start += 1
        
print(final)
           
           
           