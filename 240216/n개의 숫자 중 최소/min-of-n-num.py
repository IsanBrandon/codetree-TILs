N = int(input())
arr = list(map(int, input().split()))

min_val = arr[0]
for elem in arr:
    if min_val >= elem:
        min_val = elem

print(min_val, end=" ")

cnt = 0

for elem in arr:
    if min_val == elem:
        cnt += 1

print(cnt)