def least_min(a, b, c):
    return min(a, b, c)

a, b, c = tuple(map(int, input().split()))

print(least_min(a, b, c))