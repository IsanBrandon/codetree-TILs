n = int(input())

def get_sum(n):
    if n < 10:
        return n * n

    digit = (n % 10)
    return get_sum(n // 10) + digit * digit

print(get_sum(n))