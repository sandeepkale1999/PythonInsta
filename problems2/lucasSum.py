
def lucasSum(N):
    def fibo(n):
        if n == 1:
            return 2
        elif n == 2:
            return 1
        else:
            return fibo(n-1)+fibo(n-2)
        

    num = fibo(N+1)
    print(num)
    s = 0
    for i in str(num):
        s += int(i)
    return s
    

print(lucasSum(16))
