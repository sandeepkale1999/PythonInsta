# shift elements of an array by n towards left or rith..
# very important logic. 

def right_shift(arr,n):
    for i in range(n):
        arr.insert(0,arr.pop())
    return arr
     
def left_shift(arr,n):
    for i in range(n):
        arr.append(arr.pop(0))
    return arr
        
arr = [1,2,3,4,5]
n = 2
print(right_shift(arr,n))
arr = [1,2,3,4,5]
print(left_shift(arr,n))