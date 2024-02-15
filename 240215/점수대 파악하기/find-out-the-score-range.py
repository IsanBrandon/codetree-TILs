arr = list(map(int, input().split()))

count_arr = [0] * 11

for elem in arr:
    count_arr[elem // 10] += 1

for i in range(11, 1, -1):
    print(f"{(i - 1) * 10} - {count_arr[i-1]}")