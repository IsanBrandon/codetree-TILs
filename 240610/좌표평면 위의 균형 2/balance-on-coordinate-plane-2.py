MAX_X = 100

n = int(input())
points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = MAX_X
for i in range(MAX_X + 1):
    for j in range(MAX_X + 1):
        
        Q1, Q2, Q3, Q4, cnt = 0, 0, 0, 0, 0
        for x, y in points: 
            if x >= i and y >= j:
                Q1 += 1
            if x < i and y >= j:
                Q2 += 1
            if x < i and y < j:
                Q3 += 1
            if x >= i and y < j:
                Q4 += 1 
        
        cnt = max(Q1, Q2, Q3, Q4)
        ans = min(cnt, ans) 

print(ans)