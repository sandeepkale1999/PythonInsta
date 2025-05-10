# Zensar program.

arr = [1,2,2,9,4,1]

id = 0
while id < len(arr):
    if sum(arr[:id]) == sum(arr[id+1:]):
        print(arr[id],sum(arr[:id]))
        break
    id += 1
    
'''I think I need to stop this online online program. It will lead nothing yar, only insecurities'''    