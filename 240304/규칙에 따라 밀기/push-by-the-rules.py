string = input()
commend = input()

leng_com = len(commend)
list_str = list(string)
leng_str = len(string)

for i in range(leng_com):
    if commend[i] == 'L':
        front = list_str[0]
        for i in range(1, leng_str):
            list_str[i - 1] = list_str[i]
        list_str[leng_str - 1] = front

    else:
        back = list_str[leng_str - 1]
        for i in range(leng_str - 1, 0, -1):
            list_str[i] = list_str[i - 1]
        list_str[0] = back

print("".join(list_str))