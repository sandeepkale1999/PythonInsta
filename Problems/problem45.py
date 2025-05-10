 

## remove elements from a dictionary whos values are repeating. 
 
dic = {'A':'a', 'B':'b', 'C':'c', 'D':'c', 'E':'e', 'F':'b'}
## output -- {'A': 'a', 'E': 'e'}

values = list(dic.values())
v_set = set(values)

## a fucntion to get key for given value
def get_key(val):
    for k,v in dic.items():
        if val == v:
            return k
  
for i in v_set:
    if values.count(i)>1:
        rep = i 
        for m in range(values.count(i)):  
            target = get_key(rep)
            del dic[target]

print(dic)



