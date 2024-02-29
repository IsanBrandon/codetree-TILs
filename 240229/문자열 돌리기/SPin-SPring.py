string = input()
L = len(string)
print(string)

for _ in range(L):
    string = string[-1] + string[:-1]
    print(string)