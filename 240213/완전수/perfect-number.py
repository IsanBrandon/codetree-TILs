arr = input().split()
start, end = int(arr[0]), int(arr[1])
cnt = 0

for i in range(start, end+1, 1):
    sum_val = 0
    for j in range(1, i, 1):
        if i % j == 0:
            sum_val += j
    if sum_val == i:
        cnt += 1
print(cnt)