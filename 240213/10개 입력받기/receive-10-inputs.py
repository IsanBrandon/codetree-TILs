arr = list(map(int, input().split()))
cnt = 0
sum_val = 0

for i in arr:
    if i == 0:
        break
    else:
        cnt += 1
        sum_val += i

print(f"{sum_val} {sum_val / cnt :.1f}")