

n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    arr = [int(i) for i in input().split()]
    print(a,b)
    m = arr[b-1]
    arr.sort()
    print(arr)
    print(arr.index(m)+1)
