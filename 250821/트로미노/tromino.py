n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# Please write your code here.

max_sum, curr_sum = 0, 0

for row in range(n):
    for col in range(m):
        # type A module runs
        if row + 2 <= n-1 and col + 2 <= m-1:
            # type A-a
            curr_sum += grid[row][col] + grid[row][col+1] + grid[row][col+2]
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0
            # type A-b
            curr_sum += grid[row][col] + grid[row+1][col] + grid[row+2][col]
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0

        if row + 2 <= n-1 and col + 2 > m-1:
            # only type A-a
            curr_sum += grid[row][col] + grid[row+1][col] + grid[row+2][col]
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0

        if row + 2 > n-1 and col + 2 <= m-1:
            # only type A-b
            curr_sum += grid[row][col] + grid[row][col+1] + grid[row][col+2]
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0
            
        # type B module runs
        if row + 1 <= n-1 and col + 1 <= m-1:
            # type B-a
            curr_sum = grid[row][col] + grid[row+1][col] + grid[row+1][col+1]
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0
            # type B-b
            curr_sum = grid[row][col] + grid[row][col+1] + grid[row+1][col+1]
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0
            # type B-c
            curr_sum = grid[row][col] + grid[row][col+1] + grid[row+1][col]
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0
            # type B-d
            curr_sum = grid[row+1][col] + grid[row+1][col+1] + grid[row][col+1]
            max_sum = max(curr_sum, max_sum)
            curr_sum = 0

print(max_sum)