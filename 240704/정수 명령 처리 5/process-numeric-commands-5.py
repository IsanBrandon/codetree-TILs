n = int(input())
arr = []

for _ in range(n):
    qury, n = tuple(input().split())
    n = int(n)
    if qury == 'push_back':
        arr.append(n)
    elif qury == 'pop_back':
        arr.pop()
    elif qury == 'size'
        print(len(arr))
    else:
        print(arr[n - 1])