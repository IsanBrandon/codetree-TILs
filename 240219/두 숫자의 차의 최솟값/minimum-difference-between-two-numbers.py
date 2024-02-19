n = int(input())
nums = list(map(int, input().split()))

min_difference = 100

for i in range(n):
    for j in range(i+1, n):
        difference = 0 
        if nums[i] >= nums[j]:
            difference = nums[i] - nums[j]
        else:
            difference = nums[j] - nums[i]
        if difference <= min_difference: 
            min_difference = difference

print(min_difference)