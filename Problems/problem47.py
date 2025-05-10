

def costToSwap(word1, word2):
    sum = 0
    for i in range(len(word1)):
        x = ord(word1[i])
        y = ord(word2[i])
        z = (x-y)
        sum = sum+z
        
    return sum 
    
    
    
    
    
    
    
    
print(costToSwap('smile','smoke'))
    