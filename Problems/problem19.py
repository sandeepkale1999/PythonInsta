

def main(num):
    num_list = [int(i) for i in str(num)]

    for i,j in enumerate(num_list):
        if num_list.count(i) == j:
            continue
        else:
            return 'NO'
            
    return 'YES'
        

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for num in arr:
    print(main(num))
    
    
    
    
 