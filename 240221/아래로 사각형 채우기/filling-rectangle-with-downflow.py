n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    num = 1 + i
    for j in range(n):
        arr_2d[i][j] += num
        num += n
        print(arr_2d[i][j], end=" ")
    print()