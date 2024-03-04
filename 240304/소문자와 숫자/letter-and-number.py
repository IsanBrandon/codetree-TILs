string = input()

for elem in string:
    if (elem >= 'A' and elem <= 'Z') or (elem >= 'a' and elem <= 'z'):
        print(elem.lower(), end="")
    elif (elem >= '0' and elem <= '9'):
        print(elem, end="")