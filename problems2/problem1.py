
def main(n,arr):
    start = min(arr)
    end = max(arr)
    c = 0
    for i in range(start,end+1):
        if i not in arr:
            c += 1
    return c    
        
print(main(3,[5,4,6]))
print(main(4,[4,3,2,6]))
 