# wirte a program to get the pythagorian triplets in given range.

def pythaTriplets(n):
    triplets = []
    for i in range(1,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                isq = i**2
                jsq = j**2
                ksq = k**2
                if isq == jsq+ksq or jsq == isq+ksq or ksq == isq+jsq:
                    triplets.append((i,j,k))
    return triplets
    
# by list comprehension       
def pythaTriplets2(n):
    triplets = [(arr[i],arr[j],arr[k]) for i in range(1,n) for j in range(i+1,n) for k in range(j+1,n) if arr[i]**2 == arr[j]**2+arr[k]**2 or arr[j]**2 == arr[i]**2+arr[k]**2 or arr[k]**2 == arr[j]**2+arr[i]**2]
    return triplets


n = 20
print(pythaTriplets(n))
print(pythaTriplets(n))