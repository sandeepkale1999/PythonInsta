'''Incomplete'''
def main():
    area = []
    dim = []
    n = int(input())
    for _ in range(n):
        (a,b) = map(int, input().split())
        area.append(a*b)
        dim.append((a,b))
        
        
        
arr = [3,18,20,10]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        print(arr[i], arr[j], abs(arr[i]-arr[j]))



'''input: 
5
2 3
5 4
6 1
8 2
3 6
'''
