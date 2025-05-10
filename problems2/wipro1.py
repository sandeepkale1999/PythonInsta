## wipro problem 


  

strr = '43425' 
mid = len(strr)//2

 
left = strr[:mid]
right = strr[mid:][::-1]
print(left,right)

final = ''
for i in range(mid):
    final += str(int(right[i])+int(left[i]))

if len(strr)%2 == 0:
    print(final)
else:
    print(final+strr[mid])
    
