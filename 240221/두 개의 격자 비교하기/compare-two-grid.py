n, m = tuple(map(int, input().split()))

arr_2d_1st = [
    list(map(int, input().split()))
    for _ in range(n)
] 

arr_2d_2nd = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr_2d_3rd = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if arr_2d_1st[i][j] != arr_2d_2nd[i][j]:
            arr_2d_3rd[i][j] += 1
        print(arr_2d_3rd[i][j], end=" ")
    print()