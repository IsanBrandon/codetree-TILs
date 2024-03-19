n = int(input())

def print_stars(n):
    if n == 0:
        return

    for _ in range(n):
        print("*", end=" ")
    print()

    print_stars(n-1)

    for _ in range(n):
        print("*", end=" ")
    print()

print_stars(n)