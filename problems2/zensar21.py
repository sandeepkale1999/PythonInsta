# Zensar problem based on array rotation

def rot13(ch,n):
    alphs = [chr(x+97) for x in range(26)]
    ic = alphs.index(ch)
    for i in range(n):
        alphs.insert(0,alphs.pop())
    return alphs[ic]
    
 
strr = 'Hello World!'
n = 13
alphs = [chr(x+97) for x in range(26)]

final = ''
for ch in strr:
    if ch == ch.lower() and ch in alphs:
        final += rot13(ch,n)
    elif ch == ch.upper() and ch.lower() in alphs:
        final += rot13(ch.lower(),n).upper()
    else:
        final += ch
        
print(final)
