r, c = tuple(map(int, input().split()))
grid = [
    list(input().split())
    for _ in range(r)
]

# 이동 시에 행과 열이 전부 증가하도록
# 모든 쌍을 다 잡아봅니다.
cnt = 0
for i in range(1, r):
    for j in range(1, c):
        for k in range(i + 1, r - 1):
            for l in range(j + 1, c - 1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수를 세줍니다. 
                if grid[0][0] != grid[i][j] and \
                   grid[i][j] != grid[k][l] and \
                   grid[k][l] != grid[r - 1][c - 1]:
                    cnt += 1

print(cnt)


# max_cnt = 0
# for i in range(n):
#     for j in range(n - 1):
#         for k in range(i + 1, n):
#             for l in range(n - 1):
#                 max_cnt = max(max_cnt, arr[i][j] + arr[i][j + 1] \
#                                     + arr[k][l] + arr[k][l + 1])

# print(max_cnt)