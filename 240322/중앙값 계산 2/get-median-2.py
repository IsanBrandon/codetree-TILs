n = int(input())
arr = list(map(int, input().split()))
arr.sort()





for i in range(n):
    if i % 2 == 0:
        print(arr[i//2], end=" ")