nums = list(map(int, input().split()))
nums.sort()

a, b, c = nums[0], nums[1], nums[2]
d = nums[-1] - (a + b + c)
print(a, b, c, d)