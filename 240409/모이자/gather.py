import sys
INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

min_val = INT_MAX
for i in range(n):

    sum_diff = 0
    for j in range(n):
        sum_diff += arr[j] * abs(i - j)

    min_val = min(min_val, sum_diff)

print(min_val)

# max_sum = 0
# for i in range(n):
#     arr[i] *= 2

#     sum_diff = 0
#     for j in range(n - 1): 
#         sum_diff += abs(arr[j + 1] - arr[j])

#     max_sum = max(max_sum, sum_diff)
#     arr[i] //= 2

# print(max_sum)