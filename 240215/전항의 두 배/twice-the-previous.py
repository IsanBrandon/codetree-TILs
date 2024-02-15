n1, n2 = tuple(map(int, input().split()))
arr = [n1, n2]

for i in range(2, 10, 1):
    arr.append(arr[i-1] + 2 * arr[i-2])

for elem in arr:
    print(elem, end=" ")