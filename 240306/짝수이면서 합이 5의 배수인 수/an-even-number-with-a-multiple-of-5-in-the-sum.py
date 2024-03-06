def is_magic_number(n):
    tens = n // 10
    units = n % 10
    return tens + units 

n = int(input())

if is_magic_number(n) % 5 == 0:
    print("Yes")
else:
    print("No")