import sys

INT_MIN = -sys.maxsize

n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

ans = INT_MIN
for i in range(n - k + 1):
    max_val = 0
    for j in range(i, i + k):
        max_val += arr[j]
    ans = max(ans, max_val)

print(ans)