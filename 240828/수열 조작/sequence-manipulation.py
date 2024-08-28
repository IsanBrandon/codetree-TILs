from collections import deque

# 변수 선언 및 입력:
n = int(input())
dq = deque()

for i in range(1, n + 1):
    dq.append(i)

while len(dq) > 1:
    dq.popleft()
    dq.append(dq[0])
    dq.popleft()

print(dq[0])