import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


# 두 점 사이의 거리의 제곱 값을 반환합니다.
def dist(i, j):
    x1, y1 = points[i]
    x2, y2 = points[j]
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)


# 모든 쌍에 대해서 거리 제곱값을 계산하여
# 그 중 최솟값을 찾습니다.
min_dist = INT_MAX
for i in range(n):
    for j in range(i + 1, n):
        min_dist = min(min_dist, dist(i, j))

print(min_dist)


###### MINE ######
# ans = INT_MAX
# for i in range(n):
#     for j in range(i + 1, n):
#         distance = 0

#         x1, y1 = points[i]
#         x2, y2 = points[j]
#         distance = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
#         ans = min(ans, distance)

# print(ans)