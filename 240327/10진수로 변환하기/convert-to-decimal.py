bi = input()
num = 0

binary = []

for elem in bi:
    binary.append(int(elem))

len_bi = len(binary)

for i in range(len_bi):
    num = num * 2 + binary[i]

print(num)