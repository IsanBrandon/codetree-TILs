n, q = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

for _ in range(q):
    quest = list(map(int, input().split()))
    
    if quest[0] == 1:
        a = quest[1]
        print(arr[a - 1])

    elif quest[0] == 2:
        a = quest[1]
        idx = -1
        if a in arr:
            idx = arr.index(a)
        print(idx + 1)

    else:
        a = quest[1]
        b = quest[2]
        for i in range(a - 1, b):
            print(arr[i], end=" ")
        print()