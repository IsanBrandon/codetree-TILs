a, b, c = tuple(map(int, input().split()))
# temp_a, temp_b = a, b

ans = 0

# a를 몇 회 사용할지 전부 시도해 봅니다.
# 모든 경우의 수에 대해 최대가 되도록 하는 수를 계산합니다.
for i in range(c // a + 1):
    # a를 i회 사용합니다.
    cnt = a * i 

    # 값을 최대로 하기 위해 b를 몇 회 사용해야 하는지 계산합니다. 
    num_b = (c - cnt) // b

    cnt += num_b * b 

    ans = max(ans, cnt) 

print(ans) 


# for i in range(1000):
#     a *= i
#     for j in range(1000):
#         sum_num = 0
#         b *= j

#         if a + b > c:
#             break 
#         else:
#             sum_num = a + b
    
#         ans = max(ans, sum_num)
#         if j == 0:
#             b = temp_b
#         else:
#             b //= j 

#     if i == 0:
#         a = temp_a
#     else:
#         a //= i

print(ans)