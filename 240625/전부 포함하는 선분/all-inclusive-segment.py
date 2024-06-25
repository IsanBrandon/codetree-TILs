import sys
INT_MAX = sys.maxsize

n = int(input())
lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = INT_MAX

for i in range(n):
    leftest = INT_MAX
    rightest = - (INT_MAX)
    for j in range(n):
        if i == j :
            continue
        else:
            left, right = lines[j]
            leftest = min(leftest, left)
            rightest = max(rightest, right)
    ans = min(ans, (rightest - leftest))

print(ans)