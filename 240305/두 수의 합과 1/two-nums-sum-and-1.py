a, b = tuple(map(int, input().split()))

ab = a + b
ab = str(ab)
cnt = 0

for elem in ab:
    if elem == '1':
        cnt += 1

print(cnt)