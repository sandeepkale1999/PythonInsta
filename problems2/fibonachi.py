# nth fibonachi number 
def fibo(n):
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
    

for i in range(1,12):
    print(fibo(i), end = ' ')
    