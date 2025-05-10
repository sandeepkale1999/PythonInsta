def ArrayChallenge(arr):
    a,b = arr[0], arr[1]
    c,d = arr[2], arr[3]
    x = arr[-1]
    k = 0
    for i in range(a,b+1):
        for j in range(c,d+1):
            if i == j:
                k += 1
    if k == x:
        return 'true'
    else:
        return 'false'






arr = [1,8,2,4,4]
print(ArrayChallenge(arr))
