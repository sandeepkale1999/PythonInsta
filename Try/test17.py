
def ArrayChallenge(strArr):
    strr = strArr
    arr1 = [int(i) for i in strr[0][1:-1].split(',')]
    arr2 = [int(i) for i in strr[1][1:-1].split(',')]

    i = 0
    str2 = ''
    while i < len(arr1):
        str2 += str(arr1[i])+'-'+str(arr2[i])
        i += 1
        
    print(str2)
    
    
    
arr = ['[1,2,5,6]', '[5,2,8,11]']
print(ArrayChallenge(arr))
