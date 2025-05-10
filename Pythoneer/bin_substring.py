
# count the substrings in given binary string which have equal number of zeros and ones and
# zeros and ones are consecutive

# function to check if zeros and ones are consecutive in givne string
def consecutiveOnesZeros(strr):
    i = 0
    c = 1
    for j in range(1,len(strr)):
        if strr[i] != strr[j]:
            c += 1
        i += 1
    return c == 2
    
# function to get all substring of given string
def getSubstrings(sb):
    sbs = []
    c = 0
    while c <= len(bs):
        i = 0
        j = c+1
        while j <= len(bs):
            sbs.append(bs[i:j])
            i += 1
            j += 1
        c += 1
    return sbs
 
bs = '011001' # input
count = 0
for s in getSubstrings(bs):
    if s.count('1') == s.count('0') and consecutiveOnesZeros(s):
        count += 1
        
print(count)




strr = '00001111'
print(consecutiveOnesZeros(strr))
        

    
        
