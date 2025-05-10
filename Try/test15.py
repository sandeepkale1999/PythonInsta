

dic = {1:10, 2:10, 3:10, 4:20, 5:20, 6:20, 7:30, 8:30, 9:30, 10:30}

arr1 = []
arr2 = []
prev = None
for k,v in dic.items():
    pres = v
    if pres == prev:
        arr2.append((k,v))
    else:
        arr1.append((k,v))
    
    prev = pres
    
print(arr1)
print(arr2)
    