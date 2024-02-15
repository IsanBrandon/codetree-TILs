a, b = tuple(map(int, input().split()))

count_arr = [0] * 10
sum_val = 0

while True:
    count_arr[(a % b)] += 1
    a //= b
    if a <= 1:
        break

for i in range(10):
    sum_val += (count_arr[i]) ** 2

print(sum_val)