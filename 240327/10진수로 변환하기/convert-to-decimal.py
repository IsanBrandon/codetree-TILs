binary = list(map(int, list(input())))
length = len(binary)

num = 0
for i in range(length):
    num = num * 2 + binary[i]

print(num)

### MINE ###
# bi = input()
# binary = []

# for elem in bi:
#     binary.append(int(elem))

# len_bi = len(binary)

# num = 0
# for i in range(len_bi):
#     num = num * 2 + binary[i]

# print(num)