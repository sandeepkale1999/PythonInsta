
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))

def fact2(n):
    fact = 1
    while n >= 1:
        fact *= n
        n -= 1
    return fact

print(fact(4))
