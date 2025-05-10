# count the repeating digits in the string
num = '1234512'
num_set = set(num)
print(num_set)
count = 0
for i in num_set:
    if num.count(i) > 1:
        count += 1 
        
print(count)


name = 'prodata'
print(name.replace('a',''))

