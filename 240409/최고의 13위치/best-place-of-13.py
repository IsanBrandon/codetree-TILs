n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_cnt = 0
for i in range(n):
    for j in range(n-2):
        cnt = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
        max_cnt = max(max_cnt, cnt)

print(max_cnt)


# for i in range(n):
#     for j in range(n - 1):
#         max_cnt = max(max_cnt, arr[i][j] + arr[i][j + 1])

# print(max_cnt)
# 0 0 0 0