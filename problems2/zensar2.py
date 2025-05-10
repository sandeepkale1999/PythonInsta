# zensar problem 

def next(ch,n):
    alphabates = list(range(26))
    for i in range(n):
        alphabates.insert(0,alphabates.pop())
    return chr(alphabates[ord(ch)-97]+97)

strr = 'Hello World!'
n = 13
alphs = [chr(x+97) for x in range(26)]

final = ''
for ch in strr:
    if ch == ch.lower() and ch in alphs:
        final += next(ch,n)
    elif ch == ch.upper() and ch.lower() in alphs:
        final += next(ch.lower(),n).upper()
    else:
        final += ch
        
print(final)

 