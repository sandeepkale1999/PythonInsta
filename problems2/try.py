print(ord('a')-96)
print(ord('A')-64)
strr = 'Hello World!'
n = 13
alphs = [chr(x+97) for x in range(26)]
 
print(alphs)
ch = 'a'
for ch in alphs:
    print(ch,ord(ch)-97)