import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = 6
numbers = list(map(int, input().split()))
# [1, 2, 3, 4, 5, 6]

def get_diff(i, j, k):
    # 두 번째 팀원의 합은 전체에서 첫 번째 팀원의 합을 빼주면 됩니다.
    sum1 = numbers[i] + numbers[j] + numbers[k]
    sum2 = sum(numbers) - sum1
    return abs(sum1 - sum2)

# 첫 번째 팀원을 만들어줍니다.
min_diff = 1000000
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            min_diff = min(min_diff, get_diff(i, j, k))

print(min_diff)