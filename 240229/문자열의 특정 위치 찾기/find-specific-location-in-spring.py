string, char = tuple(input().split())

if char in string:
    print(string.index(char))
else:
    print("No")