MAX_TEMP = 1000

n, c, g, h = tuple(map(int, input().split()))
machine = [
    tuple(map(int, input().split()))
    for _ in range(n)
]


def production(Ta, Tb, t):
    if t < Ta :
        return c
    elif Ta <= t and t <= Tb:
        return g
    else:
        return h


ans = 0
for t in range(0, MAX_TEMP + 1):
    tmp = 0
    for i in range(n):
        Ta, Tb = machine[i]
        tmp += production(Ta, Tb, t)
    ans = max(ans, tmp)

print(ans)