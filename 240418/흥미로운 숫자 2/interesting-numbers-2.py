# 변수 선언 및 입력
x, y = tuple(map(int, input().split()))

ans = 0

# 각 숫자에 대해 
# 흥미로운 숫자인지 아닌지 여부를 판단합니다.
for i in range(x, y + 1):
    # digit배열을 만들어 각 자리 숫자의 개수를 저장합니다. 
    # all_digits에는 총 자릿수의 개수를 저장합니다.
    num = i
    digit = [0] * 10
    all_digits = 0
    while(num):
        digit[num % 10] += 1
        all_digits += 1
        num //= 10

    # interesting : i가 흥미로운 숫자이면 true, 아니면 false
    interesting = False 

    # 흥미로운 숫자가 되기 위해서는,
    # 숫자 하나만 all_digits - 1회 등장해야 합니다.
    for j in range(10):
        if digit[j] == all_digits - 1:
            interesting = True

    if interesting:
        ans += 1

print(ans)


###### TRY ######
# def finder(n):
#     tmps = list(map(int, list(str(n))))
#     # print(tmps)
#     cnt = 0
#     for i in range(len(tmps) - 1):
#         if tmps[i] != tmps[i + 1]:
#             cnt += 1
#     if cnt >= 2:
#         return False
#     else:
#         return True


# ans = 0
# for i in range(x, y + 1):
#     if finder(i):
#         ans += 1

# print(ans)