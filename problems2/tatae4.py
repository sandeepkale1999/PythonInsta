# Tata elxsi coding problem

'''for a given number N you have to find out the minimum positive integer num divisible by N
    where the sum of digits of num is equal to N and num is not equal to N'''

def main(N):
    c = 1
    while True:
        c += 1
        num = N*c
        if sum([int(i) for i in str(num)]) == N:
            return num
    else:
        return -1
    
print(main(9))
    
    