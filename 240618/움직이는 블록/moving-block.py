# 변수 선언 및 입력
n = int(input())
nums = [
    int(input())
    for _ in range(n)
]

# 전체 블럭 수를 셉니다.
sum_of_nums = sum(nums)

# 평균 블럭 수 보다 더 큰 블럭에 대해서만
# 그 차이만큼 옮겨주면 됩니다. 
avg = sum_of_nums // 2 
ans = 0
for num in nums:
    if num > avg:
        ans += num - avg 

print(ans)