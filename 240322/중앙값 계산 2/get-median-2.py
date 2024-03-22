# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))

# 1. 입력 받은 번째까지 새로운 리스트에 담아내고
# 2. sorting 시킨 다음
# 3. return으로 중간값을 뽑아주기
def sorting(n):
    arr_sorted = []
    for j in range(n):
        arr_sorted.append(arr[j])
    arr_sorted.sort()
    return arr_sorted[(n // 2)]

# 답들을 담을 리스트
ans_arr = []

# 짝수번째마다 끊어서 중간값을들 답 리스트에 담기
for i in range(n):
    if i == 0:
        ans_arr.append(arr[0])
    elif i % 2 == 0:
        ans_arr.append(sorting(i))
    else:
        pass

# 답 출력하기
for elem in ans_arr:
    print(elem, end=" ")