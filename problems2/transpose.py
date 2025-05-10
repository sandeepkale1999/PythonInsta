# Transpose of a matrix
arr = [[75,76,65,87,87],
         [78,76,68,56,89],
         [67,87,78,77,65]]

arr_t = list(zip(*arr))
print(arr_t)

arr_t = [list(t) for t in arr_t]
print(arr_t)

arr_t2 = list(zip(*arr_t))
print(arr_t2)

arr_t2 = [list(t) for t in arr_t2]
print(arr_t2)