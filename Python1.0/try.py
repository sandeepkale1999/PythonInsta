arr = [[1,2,3],[4,5,6],[7,8,9]]
dic = dict.fromkeys(range(len(arr)),0)

for i in arr:
    for j in i:
        dic[i.index(j)] += j
        
print(dic)
for k in dic.values():
    print(k)
    
print(min(dic.values()))
for m in range(len(dic)):
    dic[m]-= min(dic.values())
    
print(dic)