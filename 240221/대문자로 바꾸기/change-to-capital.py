arr_2d = [
    list(map(ord, input().split()))
    for _ in range(5)
]

for i in range(5):
    for j in range(3):
        arr_2d[i][j] = chr(arr_2d[i][j] + ord('A') - ord('a') )
        print(arr_2d[i][j], end=" ")
    print()