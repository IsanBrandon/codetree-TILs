n = int(input())

def get_num(n):
    if n == 1:
        return 2
    if n == 2:
        return 4

    return (get_num(n-2) * get_num(n-1)) % 100

print(get_num(n))