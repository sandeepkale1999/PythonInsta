# referred from probelm24

# create all possible subarrays from given array 

def sub_array(arr):
    final = []
    for i in arr:
        final.append([i])
    
    y = 0
    while y <= len(arr):
        first = 0
        second = 2+y
        while second <= len(arr):
            arr1 = arr[first:second]
            final.append(arr1)
            second += 1
            first += 1
        y += 1
        
    print(final)
    
    
    
    
    
arr = [1,2,3]
print(arr)
sub_array(arr)