n = int(input())

def down_nums(n):
    if n == 0:
        return

    print(n, end=" ")
    down_nums(n-1)


def up_nums(n):
    if n == 0:
        return

    up_nums(n-1)
    print(n, end=" ")

down_nums(n)
up_nums(n)