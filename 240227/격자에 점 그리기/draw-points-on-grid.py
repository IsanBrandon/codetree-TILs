n, m = tuple(map(int, input().split()))

placed = [
    [0 for _ in range(n)]
    for _ in range(n)
]

count = 1

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    placed[r-1][c-1] = count
    count += 1

for i in range(n):
    for j in range(n):
        print(placed[i][j], end=" ")
    print()