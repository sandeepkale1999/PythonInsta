



def lastmodified(input1,input2):
   c = 0
   for i in reversed(input2):
       c += 1
       if i == 9:
          pass 
       else:
          return(len(input2)-c+1)
          
   return 0
            
    
    
    
    
    

def maxProduct(arr, n):
 
    if (n < 2):
        print("No pairs exists")
        return
     
    
    a = arr[0]
    b = arr[1]
 
    for i in range(0, n):
         
        for j in range(i + 1, n):
            if (arr[i] * arr[j] > a * b):
                a = arr[i]
                b = arr[j]
 
    print("Max product pair is: ",a,b)
     

arr = [-10,-3,5,3,-2]
n = len(arr)
maxProduct(arr, n)
