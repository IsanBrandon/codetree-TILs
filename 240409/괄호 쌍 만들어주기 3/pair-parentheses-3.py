# 변수 선언 및 입력
string = input()
leng = len(string)

# 모든 쌍을 다 잡아봅니다.
cnt = 0
for i in range(leng):
    for j in range(i+1, leng):
        if string[i] == '(' and string[j] == ')':
            cnt += 1

print(cnt)


# cnt = 0
# for i in range(leng):
#     if string[i] == '(':
#         for j in range(i + 1, leng):
#             if string[j] == ')':
#                 cnt += 1

# print(cnt)