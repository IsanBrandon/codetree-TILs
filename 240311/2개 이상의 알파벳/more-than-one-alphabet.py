string = input()
leng = len(string)

def is_magic_string(string):
    s = string[0]
    flag = False
    for i in range(1, leng):
        if string[i] != s:
            flag = True
    return flag

if is_magic_string(string):
    print("Yes")
else:
    print("No")