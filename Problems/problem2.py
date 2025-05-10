def main1():
    T = int(input())
    for i in range(T):
        (a,b) = map(int,input().split(' '))
        print(a,b)
    
def main2():
    (a,b,c,d) = map(int,input().split())
    print(a,b,c,d)
    
def main3():
    arr = list(map(int, input().split()))
    print(arr)
    
def main4():
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(int(input()))     
    print(arr)
    
    
def main5():
    arr = [int(x) for x in input().split()]
    print(arr)
    
main5()
    
   
        
    
    
    

    