stds = 3
subs = 5

marks = [[75,76,65,87,87],
         [78,76,68,56,89],
         [67,87,78,77,65]]

sub_average = []

t_matrix = zip(*marks)    # To take transpose of given matrix
marks2 = list(t_matrix)
for sub in marks2:
    sub_average.append(sum(sub)/subs)
    
print(sub_average)
print(sub_average.index(min(sub_average)))

marks2.remove(marks2[2])
print(marks2)


marks3 = list(zip(*marks2))
print(marks3)

for i in marks3:
    print(sum(i),end = ' ')
    


'''Given a list of N students every student is marked for M subjects. Each subject is denoted by an
    index value. You have to ignore the marks of that subject for which class average is list.
    after ignoring the subject return total marks of each student.'''