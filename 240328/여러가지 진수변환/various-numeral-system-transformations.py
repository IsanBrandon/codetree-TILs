n, b = tuple(map(int, input().split()))
digits = []

while True:
    if n < 4:
        digits.append(n)
        break

    digits.append(n % 4)
    n //= 4

for digit in digits[::-1]:
    print(digit, end="")