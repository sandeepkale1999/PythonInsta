# print the world from given string which has maximum repeating characters.
strr = 'today is greatest day ever'

strlist = strr.split()
dic = dict.fromkeys(strlist,0)
print(dic)
c = 0
for w in strlist:
    c = 0
    wset = list(set(list(w)))
    for ch in wset:
        if w.count(ch) > 1:
            c += 1
    dic[w] = c
    
print(dic)
print(dic.keys())
print(dic.values())
print(max(dic.values()))


def getKey(dic, val):
    for k,v in dic.items():
        if v == val:
            return k
        
maxKey = getKey(dic,max(dic.values()))
print(maxKey)
        
