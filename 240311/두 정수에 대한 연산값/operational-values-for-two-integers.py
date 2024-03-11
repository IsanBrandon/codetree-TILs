a, b = tuple(map(int, input().split()))

def modify(a, b):
    if a > b:
        a += 25
        b *= 2
        return a, b
    else:
        b += 25
        a *= 2
        return a, b

mod_a, mod_b = modify(a, b)
print(mod_a, mod_b)