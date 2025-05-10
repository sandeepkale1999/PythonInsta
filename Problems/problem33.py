
arr = [[1,2,3,4],[4,1,2,3],[1,2,3,4],[1,2,3,4]]

def sub_array(arr):
    final = []
    for i in arr:
        final.append(tuple([i]))
    
    y = 0
    while y <= len(arr):
        first = 0
        second = 2+y
        while second <= len(arr):
            arr1 = tuple(arr[first:second])
            final.append(arr1)
            second += 1
            first += 1
        y += 1
        
    return (final)


sub_arrays = [] 
def solve(M,N,A):
    for row in A:
        sub_arrays.append(sub_array(row))
        
    j = 1
    a1 = set(sub_arrays[0])
    while j < M:
        a2 = set(sub_arrays[j])
        common = (a1.intersection(a2))
        a1 = common
        j+= 1
    
    le = []
    print(common)
    for i in common:
        le.append(len(i))
    
    return max(le)
    
print(solve(3,4,arr))




def solve2(M,N,A):
    sub_arrays = [] 
    def sub_array(arr):
        final = []
        for i in arr:
            final.append(tuple([i]))
        
        y = 0
        while y <= len(arr):
            first = 0
            second = 2+y
            while second <= len(arr):
                arr1 = tuple(arr[first:second])
                final.append(arr1)
                second += 1
                first += 1
            y += 1
            
        return (final)

    for row in A:
        sub_arrays.append(sub_array(row))
        
    j = 1
    a1 = set(sub_arrays[0])
    while j < M:
        a2 = set(sub_arrays[j])
        common = (a1.intersection(a2))
        a1 = common
        j+= 1
    print(common)
    le = []
    for i in common:
        le.append(len(i))
    
    return max(le)
    
    
    
    
print(solve2(3,4,arr))

 
 



    
    