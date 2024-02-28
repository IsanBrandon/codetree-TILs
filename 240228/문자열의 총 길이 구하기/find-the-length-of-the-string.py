string = input().split()
cnt = 0

for elem in string:
    cnt += len(elem)

print(cnt)