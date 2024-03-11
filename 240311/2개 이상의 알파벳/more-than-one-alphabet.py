string = input()
leng = len(string)

def is_magic_string(string):
    s = string[0]
    for i in range(1, leng+1):
        if string[i] == s:
            return False
        else:
            return True

if is_magic_string(string):
    print("Yes")
else:
    print("No")