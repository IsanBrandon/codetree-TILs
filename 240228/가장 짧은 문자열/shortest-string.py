longstrlen = 0
shortstrlen = 20
for _ in range(3):
    string = input()
    if len(string) >= longstrlen:
        longstrlen = len(string)
    if len(string) <= shortstrlen:
        shortstrlen = len(string)

print(longstrlen - shortstrlen)