# 변수 선언 및 입력
n = int(input())

# 동적 배열 선언
v = list()

for _ in range(n):
    command = input()

    if command.startswith("push_back"):
        _, num = tuple(command.split())
        v.append(int(num))
    
    elif command.startswith("pop_back"):
        v.pop()
    elif command.startswith("size"):
        print(len(v))
    else:
        _, num = tuple(command.split())
        print(v[int(num)-1])


































# N = int(input())

# command = []
# num = []

# for _ in range(N):
#     line = input().split()
#     command.append(line[0])
#     if line[0] == "push_back" or line[0] == "get":
#         num.append(int(line[1]))
#     else:
#         num.append(0)

# # Please write your code here.
