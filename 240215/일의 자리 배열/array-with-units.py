sum_val = 0

arr[0], arr[1] = tuple(map(int, input().split()))

for i in range(3, 11):
    sum_val = arr[i - 1] + arr[i - 2]
    arr.append(sum_val % 10)

for elem in arr:
    print(elem, end=" ")