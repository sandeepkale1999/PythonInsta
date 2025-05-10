def ArrayChallenge(strArr):
    str1 = strArr[0]
    str2 = strArr[1]
    i = 0
    count = 0
    while (i<len(str1)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
    
    
    
    
arr = ['coder','codec']
print(ArrayChallenge(arr))