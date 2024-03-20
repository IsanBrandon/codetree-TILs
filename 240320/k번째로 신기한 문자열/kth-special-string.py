n, k, t = input().split()
n, k = int(n), int(k)
# len_T = len(T)

# arr = [
#     input()
#     for _ in range(n)
# ]

# arr.sort()

# ans_arr = []

# for elem in arr:
#     if elem[0] == T[0]:
#         flag = True
#         for i in range(1, len_T):
#             if elem[i] != T[i]:
#                 flag = False
#     if flag:
#         ans_arr.append(elem)

# print(ans_arr[k-1])

# a가 b로 시작하는지를 확인.
def starts_with(a, b):
    # b의 길이가 더 길 수는 없음.
    if len(a) < len(b):
        return False

    # b의 길이만큼 살펴보며, a와 문자열이 완벽히 동일한지 확인.
    return a[:len(b)] == b

words = []
for _ in range(n):
    word = input()
    if starts_with(word, t):
        words.append(word)

# 정렬을 진행. 
words.sort()

print(words[k - 1])