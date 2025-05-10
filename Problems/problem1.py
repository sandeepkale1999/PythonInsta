def main():
    # take a 2d array as input from user 
    # matrix Subjects X Students

    Students = int(input('How many students: '))  # No of students 
    Subjects = int(input('How many subjects: '))  # NO of subjects 

    matrix = []


    for i in range(Students):
        marks = list(map(int, input().split()))
        matrix.append(marks)

    # for i in range(Students):
        # marks = []
        # for j in range(Subjects):
            # marks.append(int(input()))
        # matrix.append(marks)
        
    subject_marks_total = dict.fromkeys(range(Subjects),0)

    for std in matrix:
        for sub in range(len(std)):
            subject_marks_total[sub] += std[sub]
       
    def get_key(val,dic):
        for key, value in dic.items():
            if val == value:
                return key
          
          
    min_marks_sub = get_key(min(subject_marks_total.values()), subject_marks_total)

    for std in matrix:
        std.pop(min_marks_sub)
        
    final_marks = []
    for std in matrix:
        final_marks.append(sum(std))
        
    print(final_marks)
    print('sub with min marks avg is: ',min_marks_sub)
            
main()


'''PROBLEM STATEMETN:
    Given a list of N students, every student is marked for M subjects. Each 
    student is denoted by an index value Their teacher want to ignore the 
    marks of one subjects which have least average. And return the list 
    containing total marks of each student excluding the one for which the 
    average is least.'''