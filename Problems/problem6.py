x = 1
y = 1
z = 2
n = 3 


co = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]

print(co)

arr = [[1,2],[4,5],[2,3],[6,1]]
print(sorted(arr))
arr2 = [sorted(i) for i in arr]

arr2.sort()
print(arr2)

dic = dict.fromkeys(range(10))
print(dic)

dic = dict.fromkeys(range(10), '')
print(dic)


# cook your dish here


arr = [123,456]

    
rev_arr = [int(str(i)[::-1]) for i in arr]
print(rev_arr)
