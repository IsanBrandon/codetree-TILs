n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

cnt = 0

for num in arr:
    if num == m:
        cnt += 1

print(cnt)