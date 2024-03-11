string = input()

def is_magic_string(string):
    leng = len(string)
    for i in range(leng):
        if string[i] != string[0]:
            return True
    
    return False

if is_magic_string(string):
    print("Yes")
else:
    print("No")