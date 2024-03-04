string = input()
commend = input()

list_com = list(commend)
leng_com = len(commend)

for i in range(leng_com):
    if list_com[i] == 'L':
        front = list_com[0]
        for i in range(1, leng_com):
            list_com[i - 1] = list_com[i]
        list_com[leng_com - 1] = front

    else:
        back = list_com[leng_com - 1]
        for i in range(leng_com - 1, 0, -1)
            list_com[i] = list_com[i - 1]
        list_com[0] = back

print("".join(list_com))