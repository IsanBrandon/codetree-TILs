arr = list(map(int, input().split()))
cnt = 0
sum_val = 0

for elem in arr:
    if elem == 0:
        break
    cnt += 1

for i in range(cnt):
    sum_val += arr[i]

print(sum_val)