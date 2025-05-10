
def leftShift(arr,n):
    arr2 = arr.copy()
    for i in range(n):
        arr2.append(arr2.pop(0))
    return arr2
    
def rightShift(arr,n):
    arr2 = arr.copy()
    for i in range(n):
        arr2.insert(0,arr2.pop())
    return arr2


arr = [1,2,3,4,5]
print(leftShift(arr,2))

print(rightShift(arr,2))
print(arr)