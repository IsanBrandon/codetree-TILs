x, y = tuple(map(int, input().split()))


def finder(n):
    tmps = list(map(int, list(str(n))))
    # print(tmps)
    cnt = 0
    for i in range(len(tmps) - 1):
        if tmps[i] != tmps[i + 1]:
            cnt += 1
    if cnt >= 2:
        return False
    else:
        return True


ans = 0
for i in range(x, y + 1):
    if finder(i):
        ans += 1

print(ans)