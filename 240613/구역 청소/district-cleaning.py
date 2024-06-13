# 변수 선언 및 입력
a, b = tuple(map(int, input().split()))
c, d = tuple(map(int, input().split()))


def intersecting(x1, x2, x3, x4):
    # 겹치지 않는 경우에 대한 처리를 먼저 진행합니다. 
    if x2 < x3 or x4 < x1:
        return False
    # 나머지는 전부 겹치는 경우라고 볼 수 있습니다.
    else:
        return True 

# 겹치는지를 확인합니다.
if intersecting(a, b, c, d):
    # 만약 겹치는 부분이 있다면,
    # 두 구역들 중 가장 큰 구역에서 가장 작은 구역을 빼면
    # 오늘 몇 구역이나 청소됐는지 알 수 있습니다.
    print(max(b, d) - min(a, c))
else:
    # 만약 겹치는 부분이 없다면,
    # 두 구역들을 전부 더하면
    # 오늘 몇 구역이나 청소됐는지 알 수 있습니다.
    print((b - a) + (d - c))

########################################
# cleaned = [0] * 101

# for i in range(a, b + 1):
#     cleaned[i] += 1

# for j in range(c, d + 1):
#     cleaned[j] += 1

# ans = 0
# for elem in cleaned:
#     if elem > 0:
#         ans += 1

# print(ans)