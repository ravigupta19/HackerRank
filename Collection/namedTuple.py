#Dr. John Wesley has a spreadsheet containing a list of student's IDS, marks,class  and name.
#Your task is to help Dr. Wesley calculate the average marks of the students.
#Challenge complete code in 4 lines
from collections import namedtuple
#N ,Student = int(input()), namedtuple('Student', input())
#list_of_student = [Student(*input().split()) for _ in range(N)]
#print('{:.2f}'.format(sum([int(Student.MARKS) for Student in list_of_student])/N))

#long version of code
N = int(input())
student = namedtuple('student',input())
l = [student(*input().split()) for _ in range(N)]
total = sum([student.MARKS for student in l])
average = total/N    