def order(sentence): 
    dic = {}
    for word in sentence.split():
        for let in word:
            try:
                print(int(let))
                dic[int(let)] = word
            except:
                pass
                
    print(dic)
    final = []
    for key in sorted(dic.keys()):
        final.append(dic[key])
        
    sorted_string = ' '.join(final)
    print(final)
    print(sorted_string)
    
order("is2 Thi1s T4est 3a")

# extract numbers from givne string 

string = 'sand12dee567'
def extract_int(string):
    arr = []
    for let in string:
        if let.isdigit():
            arr.append(int(let))
    return arr
            
print(extract_int(string))
        
