string = input()
length = len(string)
cnt_ee = 0
cnt_eb = 0

for i in range(length-1):
    if string[i] == 'e' and string[i + 1] == 'e':
        cnt_ee += 1
    elif string[i] == 'e' and string[i + 1] == 'b':
        cnt_eb += 1

print(cnt_ee, cnt_eb)