str1 = input()
str2 = input()

str1 = sorted(str1)
str2 = sorted(str2)

str1 = ''.join(str1)
str2 = ''.join(str2)

if str1 == str2:
    print("Yes")
else:
    print("No")