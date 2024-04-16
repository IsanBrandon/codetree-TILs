import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

# 변수 선언 및 입력
n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = INT_MAX

# 빼야하는 점의 위치를 정합니다.
for i in range(n):
    # i번 점을 제외한 나머지 점들을 포함하기 위한
    # 직사각형의 최소 넓이를 구합니다.

    # 직사각형의 최소 넓이를 구하기 위해서는,
    # 남은 점들의 x좌표 중 최소, 최대
    #            y좌표 중 최소, 최대를 구해야 합니다.
    min_x, max_x = INT_MAX, 1 
    min_y, max_y = INT_MAX, 1
    # squre = 0
    for j, (x, y) in enumerate(arr):
        # i번째 점은 제외합니다.
        if j == i:
            continue

    # for j in range(n):
    #     if j == i:
    #         continue

    #     x, y = arr[j]
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)
    
    # squre = (max_x - min_x) * (max_y - min_y)
    ans = min(ans, (max_x - min_x) * (max_y - min_y))

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