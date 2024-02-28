string = input()
leng = len(string)
encoded = ""

for i in range(leng):
    if i % 2 == 1:
        encoded += string[i]

for i in range(len(encoded)-1, -1, -1):
    print(encoded[i], end="")