arr = list(input().split())

for i in range(len(arr)):
    if arr[i] % 3 == 0:
        print(arr[i-1])