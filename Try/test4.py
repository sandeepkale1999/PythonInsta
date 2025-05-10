
a,b = map(int, input().split())

arr = list(map(int, input().split()))

if sum(arr) <= b:
    print('YES')
else:
    print('No')
    
    