
def getTuple(N,K):
    k = int(K)
    n = N
    arr = [(i,j,k) for i in range(1,n+1) for j in range(1,n+1) for k in range(1,n+1)]
    arr = sorted(arr, key = lambda x:x[0] + x[1]+x[2])
    x,y,z = arr[k-1]

    return(x+2*y+3*z)
    
    
    
 
n = 50
k = 67   
print(getTuple(50,67))