n = int(input())

def print_stars1(n):
    if n == 0:
        return

    print_stars1(n-1)
    print("* " * n)

def print_stars2(n):
    if n == 0:
        return

    print("* " * n)
    print_stars2(n-1)

print_stars2(n)
print_stars1(n)