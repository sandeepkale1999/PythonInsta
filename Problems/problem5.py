


def solve(n,m,arr):
    pairs = [(x,y) for x in arr for y in arr if x-y == 3]

    return len(pairs)
    
    
    
    
def main2(arr):
    stack = []
    dict = {}
    index = 0

    
    stack.append(arr[index])
    for j in arr[index+1:]:
        print('arr',arr)
        print(arr[index],j)
        if j == stack[-1]+1:
            stack.append(j)
            dict[index] = stack
            print(dict)
              
                
        else:
            stack = []
            index = 0
            arr = arr[arr.index(j):]
            print(arr)
               
                
            
    print(stack)
    
    
    
def main3(arr):
    data = []
    while len(arr) > 0:
        arr2 = []
        points = []
        arr2.append(arr[0])
        for i in arr[1:]:
            if arr2[-1]+1 == i:
                arr2.append(i)
                arr.remove(i)
            else:
                points.append(arr.index(i))
        data.append(arr2)   
        try:
            arr = arr[points[0]:]
        except:
            break
        
    
    
        
     
    print(arr)
    print(arr2)
    print(points) 
    print(data)
    
main3([1,2,3,4,5,6,11,7,12,8])

 
        