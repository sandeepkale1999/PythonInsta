
arr = [3,1,3,2]
arr = [3,2,2,2,2,1]
one = []
two = []

n = int(input())
arr = [int(i) for i in input().split()]
c = 0
a = 0
b = 1
while b+2 < len(arr):
    if arr[a] == arr[a+2] and arr[b] == arr[b+2]:
        pass
    else:
        c += 1
    a += 1
    b += 1
print(c)

a = list(map(int,input().split()))