


 
def maxEnergy(ener):
    arr = ener
    arr2 = []
    i = 0
    while i < len(arr):
        j = i+1
        while j < len(arr):
            arr2.append((arr[i],arr[j]))
            j += 1
        i += 1
    a,b = max(arr2)
    return a+b
     
     
     
     
arr = [9,-3,8,-6,-7,8,10]
print(maxEnergy(arr))