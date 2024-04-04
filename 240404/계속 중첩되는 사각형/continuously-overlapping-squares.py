OFFSET = 100
MAX_R = 200

n = int(input())
rects = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

checked = [
    [0] * (MAX_R + 1)
    for _ in range(MAX_R + 1)
]

for i, (x1, y1, x2, y2) in enumerate(rects, start=1):
    x1, y1 = x1 + OFFSET, y1 + OFFSET
    x2, y2 = x2 + OFFSET, y2 + OFFSET

# 1 -> red / 2 -> blue
    if i % 2 != 0:
        for x in range(x1, x2):
            for y in range(y1, y2):
                checked[x][y] = 1
    else:
        for x in range(x1, x2):
            for y in range(y1, y2):
                checked[x][y] = 2

area = 0
for x in range(MAX_R + 1):
    for y in range(MAX_R + 1):
        if checked[x][y] == 2:
            area += 1

print(area)