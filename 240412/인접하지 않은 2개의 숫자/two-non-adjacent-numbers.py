import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))

# 인접하지 않은 모든 쌍을 다 잡아봅니다. 
ans = INT_MIN
for i in range(n):
    for j in range(i + 2, n):
        if ans < arr[i] + arr[j]:
            ans = arr[i] + arr[j]

###### MINE ######
# sum_val = 0
# for i in range(n):
#     for j in range(i+2, n):
#         sum_val = arr[i] + arr[j]
#         ans = max(ans, sum_val)

print(ans)