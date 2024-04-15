import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:
n, s = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

sum_val = sum(arr)
min_gap = INT_MAX
for i in range(n): 
    for j in range(i+1, n):
        # if i == j:
        #     continue
        new_sum = sum_val - (arr[i] + arr[j])
        gap = abs(s - new_sum)
        min_gap = min(min_gap, gap)

print(min_gap)