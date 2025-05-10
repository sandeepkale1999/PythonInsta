## zensar 2

def maxNum(n,m,c):
    total = list(range(1,n+1))
    print(total)
    nc = total.copy()
    for i in c:
        nc.remove(i)
    print(nc)
    
    arr = []
    
    for i in nc:
        pr = []
        for j in c:
            p = total.index(i)-total.index(j)
            pr.append(abs(p))
        arr.append(min(pr))
        
        
    print(arr)
    print(max(arr))
    
    
    
    

n = 5 
m = 2 
c = [1,5]

n = 7
m = 4
c = [1,2,3,4]
maxNum(n,m,c)    
