string = input()

for elem in string:
    if (elem >= 'a' and elem <= 'z'):
        print(elem.upper(), end="")
    elif (elem >= 'A' and elem <= 'Z'):
        print(elem.lower(), end="")