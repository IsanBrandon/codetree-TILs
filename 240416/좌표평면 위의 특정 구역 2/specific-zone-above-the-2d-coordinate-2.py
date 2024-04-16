import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = INT_MAX
for i in range(n):
    x_min, x_max, y_min, y_max = INT_MAX, INT_MIN, INT_MAX, INT_MIN
    squre = 0
    for j in range(n):
        if j == i:
            continue

        x, y = arr[j]
        x_min, x_max = min(x_min, x), max(x_max, x)
        y_min, y_max = min(y_min, y), max(y_max, y)
    
    squre = (x_max - x_min) * (y_max - y_min)
    ans = min(squre, ans)

print(ans)



# ans = 100
# for i in range(n):
#     count = [0] * 11
#     for j in range(n):
#         if j == i:
#             continue

#         x1, x2 = segments[j]
#         for k in range(x1, x2 + 1):
#             count[k] += 1

#     max_cnt = max(count)
#     ans = min(ans, max_cnt)