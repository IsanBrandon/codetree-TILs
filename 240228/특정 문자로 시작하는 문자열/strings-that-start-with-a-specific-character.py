n = int(input())

arr = [
    input()
    for _ in range(n)
]

the_chr = input()
cnt = 0
sum_val = 0

for i in range(n):
    if arr[i][0] == the_chr:
        cnt += 1
        sum_val += len(arr[i])

print(f"{cnt} {sum_val/cnt:.2f}")