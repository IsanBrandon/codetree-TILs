def plus(n, m):
    return n + m

def minus(n, m):
    return n - m

def multiple(n, m):
    return n * m

def division(n, m):
    return n // m

a, o, c = tuple(input().split())
a, c =int(a), int(c)

if o == '+':
    print(f"{a} + {c} = {plus(a, c)}")
elif o == '-':
    print(f"{a} - {c} = {minus(a, c)}")
elif o == '/':
    print(f"{a} / {c} = {division(a, c)}")
elif o == '*':
    print(f"{a} * {c} = {multiple(a, c)}")
else:
    print("False")