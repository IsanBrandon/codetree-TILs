import sys
INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

ans = INT_MIN
sum_val = 0
for i in range(n):
    for j in range(i+2, n):
        sum_val = arr[i] + arr[j]
        ans = max(ans, sum_val)

print(ans)