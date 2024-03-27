class Student:
    def __init__(self, h, w, idx):
        self.h, self.w, self.idx = h, w, idx

n = int(input())
students = []
for i in range(1, n+1):
    h, w = tuple(map(int, input().split()))
    students.append(Student(h, w, i))

students.sort(key=lambda x: (x.h, -x.w))

for student in students:
    print(student.h, student.w, student.idx)