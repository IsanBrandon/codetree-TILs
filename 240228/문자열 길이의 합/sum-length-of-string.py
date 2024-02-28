n = int(input())

arr = [
    input()
    for _ in range(n)
]

total_len = 0
cnt_first_a = 0

for i in range(n):
    total_len += len(arr[i])
    if arr[i][0] == 'a':
        cnt_first_a += 1

print(total_len, cnt_first_a)