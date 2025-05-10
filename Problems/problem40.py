n = 3
t = 60
a = [10,10,10]
b = [10,20,30]




def getMax(N,T,A,B):
    energy = 0
    for i in range(N):
        T -= A[i]
        energy += B[i]
        if T == 0:
            break 
            
    return energy
        
        
       



       
        
print(getMax(n,t,a,b))