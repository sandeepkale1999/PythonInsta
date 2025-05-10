def main():
    def main():
        n = int(input())
        dic = {}
        for _ in range(n):
            (t,s) = map(int, input().split())
            dic[t] = s
            
            
    def get_key(val, my_dict):
        for key, value in my_dict.items():
             if val == value:
                 return key
     
            
    dic = {2: 3, 4: 1, 6: 4, 5: 2, 1: 3, 7: 3, 3: 2}

    print(sorted(dic.values()))

    for k,v in sorted(dic.items()):
        print(k,v)
        
        
        
    print(sorted(dic.values()))
    for i in sorted(dic.values()):
        print(get_key(i,dic), end = ' ')
        dic[get_key(i,dic)] = None
           
        print(dic)
        
  
def main2():
    dic = {2: 3, 4: 1, 6: 4, 5: 2, 1: 3, 7: 3, 3: 2}
    arr = [(x,y) for x,y in dic.items()]
    
    print(arr)
    arr.sort()
    print(arr)
    
    
    
    
main2()
        