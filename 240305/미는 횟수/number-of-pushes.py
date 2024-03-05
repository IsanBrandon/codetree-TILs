str_A = input()
str_B = input()

n = 0
leng = len(str_A)
flag = -1

for i in range(leng):
    str_A = str_A[-1] + str_A[:-1]
    n += 1

    if a == b:
        flag = 1
        break 

if flag == 1:
    print(n)
else:
    print(-1)