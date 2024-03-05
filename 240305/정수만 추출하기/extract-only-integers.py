a, b = input().split()

idx1 = 0
idx2 = 0

# a의 정수로 변환 가능한 최대 인덱스를 찾습니다.
for elem in a:
    if elem <= '9' and elem >= '0':
        idx1 += 1
    else:
        break

# b의 정수로 변환 가능한 최대 인덱스를 찾습니다.
for elem in b:
    if elem <= '9' and elem >= '0':
        idx2 += 1
    else:
        break

str1 = a[:idx1]
str2 = b[:idx2]


str1 = int(str1)
str2 = int(str2)

print(str1 + str2)