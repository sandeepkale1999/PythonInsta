## wipro problem 

def encrypt(num):
    b_num = str(bin(num)).lstrip('0b')
    final = ''
    for i in b_num:
        if i == '0':
            final += '1'
        else:
            final += '0'
        
    
    return int(final,2)

arr = [65,29,56,34]
for j in arr:
    print(encrypt(j))

name = 'sandeep'
print(name.replace('e','k'))

name2 = name.replace('e','k')
print(name2)

# convert a binary number into decimal 

print(int('1111',2))