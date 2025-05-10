
def diagonalSum(arr,N,M):
    summ = 0
    i = 0
    j = 0
    while i < M and j < N:
        summ += arr[i][j]
        i += 1
        j += 1
        
    x = 0
    y = 2
    while x < M and y >= 0:
        summ += arr[x][y]
        y -= 1
        x += 1
        
    middle = arr[M//2][N//2]
    summ = summ-middle
    return summ
    
arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]
    
N = 3
M = 3
print(diagonalSum(arr,N,M))
    
    
