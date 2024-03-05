num = int(input())

def sum_n_devided(n):
    sum_val = 0
    for i in range(1, n+1):
        sum_val += i
    return sum_val // 10

ans = sum_n_devided(num)

print(ans)