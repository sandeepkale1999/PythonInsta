
n = input()
arr = [int(i) for i in input().split()]
n = len(arr)
arr2 = [(arr[i], arr[j]) for i in range(n) for j in range(i+1, n)]
print(sum(max(arr2)))


# arr = [10,-3,8,-6,-7,8,11]