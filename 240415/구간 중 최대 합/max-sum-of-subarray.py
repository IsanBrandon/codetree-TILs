# import sys

# INT_MIN = -sys.maxsize

# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

# 모든 구간의 시작점을 잡아봅니다.
# ans = INT_MIN
max_sum = 0
for i in range(0, n - k + 1):
    # 해당 구간 내 원소의 합을 구합니다.
    # max_val = 0
    interval_sum = 0 
    for j in range(i, i + k):
    #    max_val += arr[j]
        interval_sum += arr[j]

    # 최댓값을 구합니다.
    # ans = max(ans, max_val)
    max_sum = max(max_sum, interval_sum)

# print(ans)
print(max_sum)