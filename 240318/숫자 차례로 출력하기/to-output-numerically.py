n = int(input())

def down_num(n):
    if n == 0:
        return

    down_num(n - 1)
    print(n, end=" ")

def up_num(n):
    if n == 0:
        return

    print(n, end=" ")
    up_num(n - 1)

down_num(n)
print()
up_num(n)