
## sum of digits until it becomes unit digit 
num = 888 ## 24 -> 6 
def intSum(n):
    global s 
    s = n
    if len(str(n)) > 1:
        s = sum([int(i) for i in str(n)])
        intSum(s)
    return s
    
print(intSum(81))

def intsum(n):
    if n > 0:
        while len(str(n)) > 1:
            k = sum([int(i) for i in str(n)])
            n = k
            
        return k
    else:
        return -1
        
print(intsum(888))
print(intsum(0))