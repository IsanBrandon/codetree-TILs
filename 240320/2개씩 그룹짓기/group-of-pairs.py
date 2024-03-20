n = int(input())
nums = list(map(int, input().split()))

# nums를 정렬
nums.sort()

group_max = 0
for i in range(n):
    # i번째와 2n - 1 -i번째 원소를 매칭.
    group_sum = nums[i] + nums[2*n - 1 - i]
    if group_sum > group_max:
        # 최댓값을 갱신.
        group_max = group_sum

print(group_max)




# print(max(arr) + min(arr)) -> 내가 생각했던 거