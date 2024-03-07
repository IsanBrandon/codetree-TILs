a, b = tuple(map(int, input().split()))

def is_magic_number(n, m):
    cnt = 0
    for i in range(n, m+1):
        if i % 2 != 0 and i % 10 != 5 and (i % 3 != 0 or i % 9 == 0):
            cnt += 1
    return cnt


print(is_magic_number(a, b))