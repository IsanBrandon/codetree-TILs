n = int(input())
x = 'A'

for i in range(n):
    for j in range(n):
        print(chr(ord(x) + j), end="")
    print()