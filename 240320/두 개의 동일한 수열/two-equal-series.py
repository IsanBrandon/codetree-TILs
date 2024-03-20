n = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort()

flag = True

for i in range(n):
    if arrA[i] != arrB[i]:
        flag = False

if flag:
    print("Yes")
else:
    print("No")