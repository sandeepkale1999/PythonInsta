# Tata elxi problem based on fibonachi series

# nth fibonachi element
def fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return(fibo(n-1) + fibo(n-2))
    


def main(strr):
    sam = 0
    for i in strr.lower():
        sam += fibo(ord(i)-97)
    return sam

strr = 'MAN'    
print(main(strr))
strr = 'MORE'
print(main(strr))

print(ord('a')-96)