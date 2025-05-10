def main():
    Students = int(input())
    Subjects = int(input())

    matrix = []

    for i in range(Students):
        a = []
        for j in range(Subjects):
            a.append(int(input()))
        matrix.append(a)
        
matrix = [[50,30,70],[30,70,99],[99,20,30]]   
Subjects = 3
Students = 3

   
dic = dict.fromkeys(range(Subjects),0)

for i in matrix:
    for j in i:
        dic[i.index(j)] += j
        
print(dic)
    

def get_key(val):
    for key, value in dic.items():
        print(key, value, val)
        if value == val:
            return key
            
min_sub_key = get_key(min(dic.values()))
 
for x in matrix:
    x.pop(min_sub_key)
    
print(matrix)

final_marks = []
for y in matrix:
    final_marks.append(sum(y))
    
print(final_marks)