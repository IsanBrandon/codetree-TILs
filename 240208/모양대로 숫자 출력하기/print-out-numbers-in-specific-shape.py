n = int(input())

for i in range(n):
    for _ in range(i):
        print(" ", end=" ")

    for j in range(n-i):
        print(n-i-j, end=" ")

    print()