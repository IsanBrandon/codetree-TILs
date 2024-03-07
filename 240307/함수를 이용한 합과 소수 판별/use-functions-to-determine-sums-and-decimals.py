a, b = tuple(map(int, input().split()))

def is_miracle_number(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def is_digit_sum_even(n):
    digit_sum = (n // 100) + ((n // 10) % 10) + (n % 10)
    if digit_sum % 2 == 0:
        return True
    return False

cnt = 0
for i in range(a, b+1):
    if is_miracle_number(i) and is_even(i):
        cnt += 1

print(cnt)