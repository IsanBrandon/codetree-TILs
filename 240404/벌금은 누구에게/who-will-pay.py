n, m, k = tuple(map(int, input().split()))

arr = [k] * (n + 1)

ans = 0
for _ in range(m):
    minus_num = int(input())
    arr[minus_num] -= 1
    if arr[minus_num] == 0:
        ans = minus_num
        break
print(ans)