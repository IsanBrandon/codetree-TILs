n = int(input())

def get_ans(a):
    if a == 1:
        return 0
    
    if a % 2 == 0:
        return get_ans(a // 2) + 1
    else:
        return get_ans(3 * a + 1) + 1

print(get_ans(a))