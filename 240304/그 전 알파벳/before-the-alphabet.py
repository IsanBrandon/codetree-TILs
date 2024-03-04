char = input()

if char == 'a':
    next_chr = ord(char) + 25
else:
    next_chr = ord(char) - 1

print(chr(next_chr))