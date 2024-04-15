# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
arrA = list(map(int , input().split()))
arrB = list(map(int, input().split()))

# 모든 구간의 시작점을 잡아봅니다.
cnt = 0
for i in range(0, n - m + 1):
    if sorted(arrA[i:i+m]) == sorted(arrB):
        cnt += 1

print(cnt)