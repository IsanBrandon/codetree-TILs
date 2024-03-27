# class Distance:
#     def __init__(self, x, y, order):
#         self.x, self.y, self.order = x, y, order

# 변수 선언 및 입력
n = int(input())
distances = []

# 원점과의 거리를 계산하는 함수.
def get_dist_from_origin(x, y):
    return abs(x) + abs(y)

for i in range(n):
    x, y = tuple(map(int, input().split()))
    # 원점과의 거리와 index를 저장.
    distances.append((
        get_dist_from_origin(x, y), i + 1
    ))

distances.sort()

for _, idx in distances:
    print(idx)