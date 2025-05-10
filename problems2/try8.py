 

def getPlanetDestroy(planets):
    def check(arr):
        n = len(arr)
        odd = 0
        even = 0
        for i in range(0,n,2):
            odd += arr[i]
        for j in range(1,n,2):
            even += arr[j]
        return even == odd
    
    m = 0
    flag = False
    n = len(planets)
    while m < n:
        temp = planets.pop(m)
        if check(planets):
            flag = True
            break
        else:
            planets.insert(0,temp)
        m += 1
    if flag:
        return m
    else:
        reurn -1
        
        
       
    
    
    
    
    
    
    
    
planets = [2,4,6,3,4]
print(getPlanetDestroy(planets))