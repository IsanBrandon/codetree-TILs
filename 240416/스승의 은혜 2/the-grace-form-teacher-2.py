n, b = tuple(map(int, input().split()))
arr = [
    int(input())
    for _ in range(n)
]

sorted_arr = sorted(arr)

curr_exp = 0
cnt = 0
feasibility = 0
for i in range(n):
    curr_exp += arr[i]
    cnt += 1

    if curr_exp >= b:
        curr_exp -= arr[i]
        cnt -= 1
        feasibility = arr[i] // 2
        if curr_exp + feasibility > b:
            print(cnt)
            break
        else:
            cnt += 1
            print(cnt)
            break