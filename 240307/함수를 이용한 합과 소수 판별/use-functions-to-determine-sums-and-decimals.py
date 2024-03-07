a, b = tuple(map(int, input().split()))

def is_miracle_number(n):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
    return flag 

def is_even(n):
    if ((n//10) + (n%10)) % 2 == 0:
        return True

cnt = 0
for i in range(a, b+1):
    if is_miracle_number(i) and is_even(i):
        cnt += 1

print(cnt)