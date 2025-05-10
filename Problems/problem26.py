
arr = [1,4,3,4,5]

target = 3 

for i in arr[0:target-1]:
    if i > target:
        print('NO')
        break
    
else:
    print('Yes')
    
    
"""If is is normal execution of for loop without execution break statement then else block is executed 
    If loop breaks in between with break statement then else block won't executed """