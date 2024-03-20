n = int(input())

def get_ans(a):
    if a == 1:
        return 1
    if a == 2:
        return 2

    return get_ans(a // 3) + get_ans(a - 1)

print(get_ans(n))