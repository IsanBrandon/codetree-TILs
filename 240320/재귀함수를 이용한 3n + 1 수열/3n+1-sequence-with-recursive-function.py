n = int(input())

def get_ans(n):
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return get_ans(n // 2) + 1
    else:
        return get_ans(3 * n + 1) + 1

print(get_ans(n))