# 변수 선언 및 입력
n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# 삼각형의 넓이에 2를 곱한 값을 반환합니다.
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * y2 + x2 * y3 + x3 * y1) - \
                (x2 * y1 + x3 * y2 + x1 * y3))


# 3개의 점을 모두 골라보면서
# 조건을 만족하는 경우 중
# 최대 넓이를 계산합니다.
max_area = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # x값이 같은 쌍이 있으며, y값 역시 같은 쌍이 있는 경우에만
            # 최대 넓이를 계산합니다. 
            # max_area = max(max_area, get_triangle_area(i, j, k))
            x1, y1 = points[i]
            x2, y2 = points[j]
            x3, y3 = points[k]
            if (x1 == x2 or x1 == x3 or x2 == x3) and \
                (y1 == y2 or y1 == y3 or y2 == y3):
                max_area = max(max_area, \
                                area(x1, y1, x2, y2, x3, y3))

print(max_area)

###### Failure ######
# def get_triangle_area(i1, i2, i3):

#     x1, y1 = points[i1]
#     x2, y2 = points[i2]
#     x3, y3 = points[i3]
#     area = 0

#     if x1 == x2:
#         if y1 == y3:
#             area = {(x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)}
#             return area
#         elif y2 == y3:
#             area = {(x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)}
#             return area
#     if x1 == x3:
#         if y1 == y2:
#             area = {(x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)}
#             return area
#         elif y3 == y2:
#             area = {(x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)}
#             return area
#     return 0


###### CONCEPT ######
# def get_max_overlapped_nct(i1, i2, i3):
#     count = [0] * 11 # initialize
#     for i in range(n):
#         if i in [i1, i2, i3]:
#             continue

#         x1, x2 = segments[i]
#         for j in range(x1, x2 + 1):
#             count[j] += 1

#     return max(count)


# for i in range(n):
#     for j in range(i + 1, n):
#         for k in range(j + 1, n):
#             max_cnt = get_max_overlapped_nct(i, j, k)
#             ans = min(ans, max_cnt)