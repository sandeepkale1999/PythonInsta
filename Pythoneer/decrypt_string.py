
strr = 'a1b1c3'

i = 0
j = 1
res = ''
while j < len(strr):
    res += strr[i] * int(strr[j])
    i += 2
    j += 2
    
print(res)
print(res[4])
