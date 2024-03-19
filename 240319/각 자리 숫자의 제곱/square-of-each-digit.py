n = int(input())

def squar_sum(n):
    if n < 10:
        return n * n

    return squar_sum(n // 10) + ((n % 10) * (n % 10) )

print(squar_sum(n))