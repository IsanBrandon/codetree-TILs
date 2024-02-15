arr = list(map(int, input().split()))

count_arr = [0] * 100

for elem in arr: 
    if elem == 0:
        break
    count_arr[(elem // 10)] += 1

for i in range(1, 10, 1):
    print(f"{i} - {count_arr[i]}")