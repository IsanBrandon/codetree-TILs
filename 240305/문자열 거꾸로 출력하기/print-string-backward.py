for _ in range(10):
    given_ste = input()
    if given_ste == 'END':
        break
    for elem in given_ste[::-1]:
        print(elem, end="")
    print()