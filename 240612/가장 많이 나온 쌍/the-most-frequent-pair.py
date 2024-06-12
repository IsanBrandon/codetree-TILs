# 변수 선언 및 입력 
n, m = tuple(map(int, input().split()))
pairs = [
    tuple(map(int, input().split()))
    for _ in range(m)
]


def count_num(first, second): 
    cnt = 0
    # (first, second) 쌍이 (a, b) 혹은 (b, a)라면
    # 그 개수를 세줍니다.
    for a, b in pairs:
        if (first, second) in [(a, b), (b, a)]:
            cnt += 1

    return cnt 


ans = 0
# 모든 상 (i, j)를 잡아보며
# 각 쌍이 몇 번씩 나왔는지를 확인하여
# 그 중 최댓값을 계산합니다. 
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        ans = max(ans, count_num(i, j))

print(ans)

#######################################################
# n = 5
# segments = [(1, 3), (2, 4), (5, 8), (6, 9), (7, 10)]

# max_cnt = 0
# for x in range(1, 11):
#     overlapped_cnt = 0
#     for x1, x2 in segments:
#         if x1 <= x and x <= x2:
#             overlapped_cnt += 1

#     max_cnt = max(max_cnt, overlapped_cnt)