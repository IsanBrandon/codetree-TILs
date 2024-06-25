# 가로랑 세로 길이를 구한다음 두 개 중 더 긴 걸 제곱하면 될 것 같아
x1, y1, x2, y2 = list(map(int, input().split()))
a1, b1, a2, b2 = list(map(int, input().split()))

width = max(x2, a2) - min(x1, a1)
height = max(y2, b2) - min(y1, b1)

line = width if width >= height else height

print(line ** 2)