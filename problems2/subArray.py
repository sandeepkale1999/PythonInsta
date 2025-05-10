
def subArray(arr):
    sub_arrays = []
    
    y = 0
    while y <= len(arr):
        i = 0
        j = 1+y
        while j<= len(arr):
            sub_arrays.append(arr[i:j])
            i += 1
            j += 1
        y += 1
    return sub_arrays
    

arr = [1,2,3]
print(subArray(arr))
