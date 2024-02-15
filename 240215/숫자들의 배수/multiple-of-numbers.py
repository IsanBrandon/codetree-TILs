n = int(input())
cnt = 0
arr = [n * i for i in range(1, 51, 1)]

for elem in arr:
    if elem % 5 == 0:
        cnt += 1
    print(elem, end=" ")
    if cnt == 2:
        break