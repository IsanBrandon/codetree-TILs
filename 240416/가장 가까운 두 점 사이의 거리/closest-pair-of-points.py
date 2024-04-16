import sys

INT_MAX = sys.maxsize

n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = INT_MAX
for i in range(n):
    for j in range(i + 1, n):
        distance = 0

        x1, y1 = points[i]
        x2, y2 = points[j]
        distance = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        ans = min(ans, distance)

print(ans)



# for i in range(n):
#     for j in range(i + 1, n):
#         count = [0] * 11 # initialize
#         for k in range(n):
#             if k == i or k == j:
#                 continue

#             x1, x2 = segments[k]
#             for l in range(x1, x2 + 1):
#                 count[l] += 1

#         max_cnt = max(count)
#         ans = min(ans, max_cnt)