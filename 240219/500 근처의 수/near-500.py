nums = list(map(int, input().split()))

max_num = 1
min_num = 500

for curr_num in nums:
    if (curr_num > max_num) and (curr_num < 500):
        max_num = curr_num

    elif (curr_num < min_num) and (curr_num > 500):
        min_num = curr_num

print(max_num, min_num)