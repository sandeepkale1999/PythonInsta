# tata elxsi program based on sub array program 

# subarray
def sub_arr(arr):
    sub_arrays = []
    
    y = 0
    while y <= len(arr):
        first = 0
        second = 1+y
        while second <= len(arr):
            arr1 = arr[first:second]
            sub_arrays.append(arr1)
            second += 1
            first += 1
        y += 1
    print(sub_arrays)
    return sub_arrays

arr = [1,2,3,4]
sub_arr(arr)
arr = [1,1,0,1]
for s in sub_arr(arr):
    if s.count(1) == s.count(0):
        print(s)
        print(len(s))
        break