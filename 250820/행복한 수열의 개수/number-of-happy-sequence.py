n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

ans = 0


if m == 1:
    print(2*n)
else:
    # checking row first
    for row in range(n):
        for col in range(n-1):
            satisfying_m = 1
            for i in range(1, n-col):
                if grid[row][col] == grid[row][col+i]:
                    satisfying_m += 1
                else:
                    break
            if satisfying_m >= m:
                ans += 1
                break

    # and then checking col
    for col in range(n):
        for row in range(n-1):
            satisfying_m = 1
            for j in range(1, n-row):
                if grid[row][col] == grid[row+j][col]:
                    satisfying_m += 1
                else:
                    break
            if satisfying_m >= m:
                ans += 1 
                break

    print(ans)