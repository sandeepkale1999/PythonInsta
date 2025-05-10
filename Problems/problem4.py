

def countHillValley(b_string):
    if len(b_string) != 0:
        b_string2 = b_string.rstrip(b_string[-1]).lstrip(b_string[0])
        hills = b_string2.count('1')
        valleys = b_string2.count('0')
    return hills, valleys
    
        
   
def HillValleys(hills, valleys):
    b_string = ''
    c = 0
    v1 = 0
    v2 = 0
    while len(b_string) < 320:
        if hills%2 != 0:
            
            if c%2 == 0:
                b_string += '0'
            else:
                b_string += '1'
            c+=1
            if len(b_string) >= hills+valleys:
                (v1,v2) = countHillValley(b_string)
            
                
            if v1 == hills and v2 == valleys:
                break
       
        else:
             
            if c%2 == 0:
                b_string += '1'
            else:
                b_string += '0'
            c+=1
            if len(b_string) >= hills+valleys:
                (v1,v2) = countHillValley(b_string)
            
                
            if v1 == hills and v2 == valleys:
                break
    print(len(b_string))
    print(b_string)
    

try:
    N = int(input())
except EOFError:
    pass
    
for x in range(N):
    try:
        (a,b) = map(int,input().split(' '))
        HillValleys(a,b)
    except EOFError:
        pass
  


