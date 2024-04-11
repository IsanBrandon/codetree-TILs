import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

###### MINE ######################################################
# 난 건너뛴 포인트를 제외한 배열을 새로 만들어서 문제를 풀려고 했어. #
##################################################################
# checkpoint = [
#     tuple(map(int, input().split()))
#     for _ in range(n)
# ]

# 각 i번째 체크포인트를 건너 뛰었을 때의 거리를 구해줍니다.
ans = INT_MAX
for i in range(1, n - 1):
    # 거리를 구합니다.
    dist = 0
    prev_idx = 0
    for j in range(1, n):
        if j == i:
            continue
        dist += abs(arr[prev_idx][0] - arr[j][0]) + abs(arr[prev_idx][1] - arr[j][1])
        prev_idx = j

    ans = min(ans, dist)

###### MINE ######################################################
# 난 건너뛴 포인트를 제외한 배열을 새로 만들어서 문제를 풀려고 했어.#
##################################################################
# for i in range(1, n-1):
#     ### i번째를 제외한 point들을 새 배열에 담기 ###
#     lazy_point = []
#     for j in range(n):
#         if j != i:
#             lazy_point.append(checkpoint[j])

#     ### 거리 계산해주기 ###
#     length = len(lazy_point)
#     dist = 0
#     for k in range(length-1):
#         x1, y1 = lazy_point[k]
#         x2, y2 = lazy_point[k+1]
#         dist += abs(x1 - x2) + abs(y1 - y2)
#     ans = min(ans, dist)

# 출력
print(ans)