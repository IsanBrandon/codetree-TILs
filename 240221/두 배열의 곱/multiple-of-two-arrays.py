arr_2d_1 = [
    list(map(int, input().split()))
    for _ in range(3)
]

input()

arr_2d_2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

arr_2d_sum = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr_2d_sum[i][j] = arr_2d_1[i][j] * arr_2d_2[i][j]
        print(arr_2d_sum[i][j], end=" ")
    print()