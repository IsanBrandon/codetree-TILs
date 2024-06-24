# 변수 선언 및 입력
nums = list(map(int, input().split()))

# 오름차순으로 정렬을 진행합니다.
nums.sort()

# 오름차순으로 정렬했을 때,
# 가장 작은 숫자는 A,
# 두 번째로 작은 숫자는 항상 B가 됩니다.
a, b = nums[0], nums[1]
# 또한, 가장 큰 숫자는 항상 A + B + C가 되므로
# C는 끝 숫자 - A - B가 됩니다.
c = nums[-1] - a - b

print(a, b, c)