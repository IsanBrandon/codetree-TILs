n, m = tuple(map(int, input().split()))

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 0

for j in range(m):
    for i in range(n):
        if j % 2 == 0:
            arr_2d[i][j] += num
            num += 1

        else:
            arr_2d[n-1-i][j] += num
            num += 1  

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()