import sys
INT_MAX = sys.maxsize

n = int(input())
checkpoint = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = INT_MAX
# if n == 3:
for i in range(1, n-1):
    ### i번째를 제외한 point들을 새 배열에 담기 ###
    lazy_point = []
    for j in range(n):
        if j != i:
            lazy_point.append(checkpoint[j])

    ### 거리 계산해주기 ###
    length = len(lazy_point)
    dist = 0
    for k in range(length-1):
        x1, y1 = lazy_point[k]
        x2, y2 = lazy_point[k+1]
        dist += abs(x1 - x2) + abs(y1 - y2)
    ans = min(ans, dist)

print(ans)