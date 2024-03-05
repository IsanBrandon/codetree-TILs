n, m = tuple(map(int, input().split()))

lcm = 0

for i in range(1, n*m+1):
    if i % n == 0 and i % m == 0:
        lcm = i    
        break

print(lcm)