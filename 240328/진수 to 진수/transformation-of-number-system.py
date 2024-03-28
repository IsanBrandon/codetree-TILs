a, b = tuple(map(int, input().split()))
a_nary = list(map(int, list(input())))
length = len(a_nary)

# a진수 -> 10진수 -> b진수
num = 0
for i in range(length):
    num = num * a + a_nary[i]

digits = []
while True:
    if num < b:
        digits.append(num)
        break

    digits.append(num % b)
    num //= b

for digit in digits[::-1]:
    print(digit, end="")