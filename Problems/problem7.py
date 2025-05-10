
def palindrom(strr):
    (x,y) = map(str,input().split())

    return strr == strr[::-1]
    
def main(strr):
    if palindrom(strr):
        return True 
    else:
        strr = list(strr)
        
            
            
 
def main2():
    inp = [str(i) for i in input().split()]
    priority = ['R','B','G']
    for p in priority:
        if p in inp:
            print(p)
            break
    
    
def main3():
    for _ in range(int(input())):
        n=int(input())
        if n%2==1:
            print(-1)
        else:
            s=""
            for i in range(n//2):
                s+="01"
            print(s)
        
        
main3()