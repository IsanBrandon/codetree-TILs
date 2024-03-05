str1 = '0'
str2 = '0'

a = input()
b = input()

for elem in a:
    if elem <= '9' and elem >= '0':
        str1 += elem

for elem in b:
    if elem <= '9' and elem >= '0':
        str2 += elem

str1 = int(str1)
str2 = int(str2)

print(str1 + str2)