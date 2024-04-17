# 변수 선언 및 입력
n, k = tuple(map(int, input().split()))

num = [
    int(input())
    for _ in range(n)
]

ans = -1

# 모든 쌍에 대해서 터질 수 있는 폭탄을 찾고
# 그 중 번호가 최대인 값을 찾습니다.
for i in range(n):
    for j in range(i + 1, n):
        # 거리가 k를 초과하는 경우 넘어갑니다.
        if j - i > k:
            break

        # 두 폭탄의 번호가 다를 경우 터지지 않습니다.
        if num[i] != num[j]:
            continue

        ans = max(ans, num[i])

print(ans)