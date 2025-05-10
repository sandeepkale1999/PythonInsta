N = 3
arr = [4,6,7]

def main(arr,N):
    c = 0
    for i in range(N):
        for j in range(i+1,N):
            if j-i == arr[j]-arr[i]:
                c += 1
    return c       
            
print(main(arr,N))
arr = [7,4,5,6]
print(main(arr,len(arr)))
