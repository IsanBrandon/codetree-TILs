str_A = input()
str_B = input()


leng = len(str_A)
cnt = 0

for i in range(leng):
    str_A = str_A[-1] + str_A[:-1]
    cnt += 1

    if str_A == str_B:
        print(cnt)
        break 

    if i == leng - 1: print("-1")