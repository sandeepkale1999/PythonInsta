

def isPrime(n):
    if n > 1:
        if n == 2:
            return True
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True


print(isPrime(9))



num = 666

def intSum(num):
    return sum([int(i) for i in str(num)])

print(intSum(num))