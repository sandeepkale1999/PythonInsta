
def MinSwaps(s):
    N = len(s)
    one = 0
    zero = 0
 
    for i in range(N):
        if (s[i] == 'G'):
            one += 1
        else:
            zero += 1
     
    if (one > zero + 1 or zero > one + 1):
        return -1
 
    if (N % 2):
       
        num = (N + 1) / 2
        one_even = 0
        zero_even = 0
 
        for i in range(N):
            if (i % 2 == 0):
                if (s[i] == 'G'):
                    one_even+=1
                else:
                    zero_even+=1
             
        if (one > zero):
            return num - one_even
 
        else:
            return num - zero_even
     
    else:
        one_odd = 0
        one_even = 0
 
        for i in range(N):
            if (s[i] == 'G'):
                if (i % 2):
                    one_odd+=1
 
                else:
                    one_even+=1
             
        return int(min(N // 2 - one_odd, N // 2 - one_even))
 
s = input()
print(int(MinSwaps(s)))