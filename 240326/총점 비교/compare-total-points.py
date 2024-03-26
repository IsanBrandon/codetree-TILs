class Student:
    def __init__(self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, kor, eng, math

n = int(input())
students = []
for _ in range(n):
    name, kor, eng, math = tuple(input().split())
    students.append(Student(name, int(kor), int(eng), int(math)))

students.sort(key=lambda x: x.kor + x.eng + x.math)

for student in students: # 정렬 이후의 결과 출력
    print(student.name ,student.kor, student.eng, student.math)

# from functools import cmp_to_key
# students = [
#     Student(90, 80, 90), # 첫 번째 학생
#     Student(20, 80, 80), # 두 번째 학생
#     Student(90, 30, 60), # 세 번째 학생
#     Student(60, 10, 50), # 네 번째 학생
#     Student(80, 20, 10), # 다섯 번째 학생 
# ]
#
# # custom comparator를 직접 정의
# # x가 앞에 있는 학생, y가 뒤에 있는 학생이라 가정했을 때
# # 이 순서가 우리가 원한나 순서라면 0보다 작은 값을,
# # 반대라면 0보다 큰 값을
# # 둘의 우선순위가 동일하다면 0을 반환하면 됩니다.
# # 보통 반환값에 1, -1, 0을 사용합니다.
# def compare(x, y):
#     # x만 30의 배수라면 x가 더 앞에 있어야 하므로
#     # 현재 순서가 옳습니다.
#     if x.kor % 30 == 0 and y.kor % 30 != 0:
#         return -1
#     # y만 30의 배수라면 y가 더 앞에 있어야 하므로
#     # 현재 순서는 틀렸습니다.
#     if x.kor % 30 != 0 and y.kor % 30 == 0:
#         return 1
#     # 우선 순위가 동일한 경우입니다.
#     return 0 

# # compare 기준에 따른 custom 정렬
# students.sort(key=cmp_to_key(compare))