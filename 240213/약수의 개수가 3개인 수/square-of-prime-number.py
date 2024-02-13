start, end = tuple(map(int, input().split()))
ans = 0

for curr_num in range(start, end+1, 1):
    divisor_cnt = 0
    for divisor in range(1, curr_num+1, 1):
        if curr_num % divisor == 0:
            divisor_cnt += 1
    if divisor_cnt == 3:
        ans += 1
print(ans)