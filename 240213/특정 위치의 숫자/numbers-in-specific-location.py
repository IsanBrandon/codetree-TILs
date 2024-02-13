arr = list(map(int, input().split()))
sum_val = 0

for i in range(10):
    if i == 2 or i == 4 or i == 9:
        sum_val += arr[i]
print(sum_val)