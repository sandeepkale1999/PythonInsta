  
  
name = 'my name is granna..'

ch = 'a'



left = name.index(ch)
right = len(name)-name[::-1].index(ch)


c = 0
for j in set(name[left:right-1]):
    if j != ' ' and j != ch:
        c += 1
        
print(c)


    
    
    
    
    