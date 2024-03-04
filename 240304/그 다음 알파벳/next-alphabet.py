char = input()


if char != 'z':
    next_chr = ord(char) + 1
else:
    next_chr = ord(char) - 25

print(chr(next_chr))