n, A = tuple(input().split())
n = int(n)
cnt = 0

for _ in range(n):
    B = input()
    if A == B:
        cnt += 1

print(cnt)