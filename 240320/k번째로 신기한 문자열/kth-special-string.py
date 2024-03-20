n, k, T = input().split()
n, k = int(n), int(k)
len_T = len(T)

arr = [
    input()
    for _ in range(n)
]

arr.sort()

ans_arr = []

for elem in arr:
    if elem[0] == T[0]:
        flag = True
        for i in range(1, len_T):
            if elem[i] != T[i]:
                flag = False
    if flag:
        ans_arr.append(elem)

print(ans_arr[k-1])