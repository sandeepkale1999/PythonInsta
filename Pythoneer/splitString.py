# a function the split givne string on the basis on numbers and characters
# suppose I have a string and I want to split on the basis on numbers and characters

def splitString(strr):
    arr = []
    bn = ''
    bs = ''
    for i in strr:
        if i.isnumeric():
            bn += i
            if bs != '':
                arr.append(bs)
            bs = ''
        if i.isalpha():
            bs += i
            if bn != '':
                arr.append(bn)
            bn = ''
        if (not i.isnumeric() and not i.isalpha()):
            arr.append(i)
    arr.append(bn)
    return arr

strr = 'San44// deep@123'   # op ['San', '/', '/', ' ', '44', '@', 'deep', '123']
print(splitString(strr))
