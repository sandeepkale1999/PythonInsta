# bs = '1C0C1C1A0'  # A & B | C ^ caluclate given expression

# a function the split givne string on the basis on numbers and characters
def splitString(bs):
    arr = []
    bn = ''
    for i in bs:
        if i.isnumeric():
            bn += i
        if i.isalpha():
            arr.append(bn)
            arr.append(i)
            bn = ''
    arr.append(bn)
    return arr
       
bs = '1C0C11111C1A01'        
print(splitString(bs))

bs = '1C0C1C1A0'
arr = splitString(bs)
res = int(arr[0])
i = 2
j = 1
while i < len(arr) and j < len(arr):
    if arr[j] == 'A':
        res = res & int(arr[i])
    if arr[j] == 'B':
        res = res | int(arr[i])
    if arr[j] == 'C':
        res = res ^ int(arr[i])
    i += 2
    j += 2
    
print(res)
 

def OperationsBinaryString(str):
    a=int(str[0])
    i=1
    while i+1<len(str):
        if str[i]=='A':
            a&=int(str[i+1])
        elif str[i]=='B':
            a|=int(str[i+1])
        else:
            a^=int(str[i+1])
        i+=2
    return a
 
    
    
