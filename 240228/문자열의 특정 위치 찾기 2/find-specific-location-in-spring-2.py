words = ["apple", "banana", "grape", "blueberry", "orange"]

given_chr = input()
cnt = 0

for elem in words:
    exsist = False
    for alpabet in elem[2:4]:
        if alpabet == given_chr:
            exsist = True
    if exsist == True:
        print(elem)
        cnt += 1

print(cnt)