# sort all the words in given sentence lexicographical order. 

def sortWords(S):
    arr = S.split()
    print(arr)
    arr2 = [list(i) for i in arr]
    print(arr2)
    for j in arr2:
        j.sort()
    print(arr2)
    
    final = ''
    for k in arr2:
        for x in k:
            final += x
        final += ' '
    
    return final
    
    
    

print(sortWords('hey welcome'))
