# zensar problem based on subarray

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
    

arr = [[4,2,-3,1,6],[-3,2,3,1,6]]
for a in arr:
    sa = subArray(a)
    for a in sa:
        if sum(a) == 0:
            print(True)
            break
    else:
        print(False)