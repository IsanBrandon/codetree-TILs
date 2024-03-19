arr = list(map(int, input().split()))
sum_val = 1

for elem in arr:
    sum_val *= elem

def get_sum(n):
    if n < 10:
        return n

    return get_sum(n // 10) + (n % 10)

print(get_sum(sum_val))