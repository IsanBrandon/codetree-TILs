import sys
INT_MAX = sys.maxsize

n, s = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

sum_val = sum(arr)
min_gap = INT_MAX
for i in range(n): 
    for j in range(n):
        if i == j:
            continue
        a = sum_val - (arr[i] + arr[j])
        gap = abs(s - a)
        min_gap = min(min_gap, gap)

print(min_gap)