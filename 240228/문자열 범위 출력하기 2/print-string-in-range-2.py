string = input()
n = int(input())
leng = len(string)

for elem in string[leng:leng-n-1:-1]:
    print(elem, end="")