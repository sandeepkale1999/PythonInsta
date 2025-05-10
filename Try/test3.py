# wipro 
inp = input()
vowels = ['a','e','i','o','u','a']
result = ''
for i in inp:

    if i.lower() in vowels:
        if i.isupper():
            result += vowels[vowels.index(i.lower())+1].upper()
        else:
            result += vowels[vowels.index(i)+1]
    else:
        result += i 
        
        
print(result)


        

