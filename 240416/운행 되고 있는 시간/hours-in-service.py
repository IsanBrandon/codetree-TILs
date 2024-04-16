MAX_NUM = 1000

# 변수 선언 및 입력
n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

ans = 0

# 빼야하는 직원을 정합니다.
for i in range(n):
    # i번 직원의 구간을 제외한 나머지 구간에서
    # 운행 되고 있는 시간을 구합니다.

    count = [0] * MAX_NUM

    for j, (l, r) in enumerate(segments):
        # i번째 구간은 제외합니다.
        if j == i:
            continue

        # 모든 구간을 카운팅합니다.
        for k in range(l, r):
            count[k] += 1

    time = 0

    for j in range(1, MAX_NUM):
        if count[j] > 0:
            time += 1

    # 운행 되고 있는 시간 중 최댓값을 구합니다.
    ans = max(ans, time)

print(ans)

    # for j in range(n):
    #     if j == i:
    #         continue
        
    #     start, finish = segments[j]
    #     for k in range(start, finish):
    #         count[k] += 1
    #     max_sheet = max(count)
    #     ans = max(ans, max_sheet)

print(ans)