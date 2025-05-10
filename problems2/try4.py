


 
def solution(S):
    strr = S
    n = len(strr)
    i = 0
    c = 0
    a = 0
    b = 0
    arr = []
    for j in range(1, n):
        
        if strr[i] == strr[j]:
            pass
        else:
            c += 1
        arr.append(c)
        i += 1
        print(arr)
        
    return c





strr = 'babaa'
print(solution(strr))
    
