n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.


for seqence in range(t):
    temp_u = u[n-1]
    temp_d = d[n-1] 
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
        d[i] = d[i - 1]
    d[0] = temp_u
    u[0] = temp_d

print(*u)
print(*d)