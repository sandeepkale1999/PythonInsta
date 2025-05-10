
## zensar problem 
## kth palindromic number 
 
def is_palindrome(n):
    return n == int(str(n)[::-1])
    
    
n = 100
k = 9
c = 1
while c <=k:
    if is_palindrome(n):
        c+=1
    n += 1

print(n-1)

def main(n,k):
    c = 0
    while True:
        if n == int(str(n)[::-1]):
            c += 1
        if c == k:
            return n
        n+=1
        
        
n = 100
k = 9        
print(main(n,k))