


def solution(a,f,m):
    s = sum(a)
    n = len(a)
    diffsum = int(m*(n+f)-s)
    if (diffsum/f) > 6:
        return 0
    else:
        avgFVal = int(diffsum/f)
        FArray = []
        for x in range(0,f):
            if (x == f-1):
                FArray.append(diffsum)
                continue
            FArray.append(avgFVal)
            diffsum -= avgFVal
            
        print(FArray)
        
        
a = [6,1]
f = 1
m = 1
solution(a,f,m)