n = int(input())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

def flag():
    # n개의 원소를 순서대로 봤을 때
    # 전부 동일한 경우에만 일치합니다.
    # 단 하나라도 다르다면, false입니다.
    for elem1, elem2 in zip(arrA, arrB):
        # 두 리스트를 한번에 받아오고 싶을 때 zip을 활용해보자.
        if elem1 != elem2:
            return False

    return True

# 정렬
arrA.sort()
arrB.sort()

# for i in range(n):
#     if arrA[i] != arrB[i]:
#         flag = False

# 수열이 일치하는지 확인.
if flag():
    # if문에 이렇게 함수를 박아둬도 된다.
    print("Yes")
else:
    print("No")