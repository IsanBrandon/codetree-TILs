import sys

INT_MAX = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))

min_diff = INT_MAX 
for i in range(n):
    arr [i] *= 2

    for j in range(n):
        remaining_arr = [elem for k, elem in enumerate(arr) if k != j]
        
        sum_diff = 0 
        for k in range(n - 2):
            sum_diff += abs(remaining_arr[k + 1] - remaining_arr[k])
        
        min_diff = min(min_diff, sum_diff) 

    arr[i] //= 2

print(min_diff) 
        

# n = 5
# arr = [1, 5, 2, 6, 8]

# max_diff = 0 
# for i in range(n):
#     arr[i] *= 2

#     for j in range(n):
#         # (METHOD3)
#         remaining_arr = [elem for k, elem in enumerate(arr) if k != j]

#         sum_diff = 0 
#         for k in range(n - 2):
#             sum_diff += abs(remaining_arr[k + 1] - remaining_arr[k])

#         max_diff = max(max_diff, sum_diff)

#     arr[i] //= 2

# print(max_diff)