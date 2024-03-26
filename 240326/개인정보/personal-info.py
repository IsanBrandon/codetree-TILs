class Student:
    def __init__(n, h, w):
        self.n, self.h, self.w = n, h, w

students = []
for _ in range(5):
    n, h, w = tuple(input().split())
    students.append(Student(n, h, w))

students.sort(key=lambda x: x.name)

print("name")
for student in students:
    print(student.name, student.h, student.w)

students.sort(key=lambda x: x.h)

print("height")
for student in students:
    print(student.name, student.h, student.w)