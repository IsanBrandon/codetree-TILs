string = input()
n = int(input())
leng = len(string)
cnt = 0

for i in range(leng - 1, -1, -1):
    # 주어진 개수만큼 출력했을 경우 탈출!
    if cnt >= n:
        break
    print(string[i], end="")
    cnt += 1