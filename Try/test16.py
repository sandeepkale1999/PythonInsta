
def StringChallenge(strParam):
    def isPalindrome(strr):
        return strr == strr[::-1]

    
    strr = strParam
    i = 0
    j = 1
    while j < len(strr):
        if isPalindrome(strr[:i]+strr[j]+strr[i]+strr[j+1:len(strr)+1]):
            return strr[:i]+strr[j]+strr[i]+strr[j+1:len(strr)+1]
        i += 1
        j += 1
        
    
    


strr = 'anna'
print(StringChallenge(strr))