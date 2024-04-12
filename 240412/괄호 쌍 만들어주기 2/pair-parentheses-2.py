string = input()
n = len(string)

cnt = 0
for i in range(n - 1):
    if string[i] == '(' and string[i + 1] == '(':
        for j in range(i + 2, n - 1):
            if string[j] == ')' and string[j + 1] == ')':
                cnt += 1

print(cnt)