MAX_NUM = 10000 

# 변수 선언 및 입력:
n = int(input())
conditions = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

# for i in range(1, MAX_X):
#     for _ in range(n):
#         i *= 2
#         for a, b in conditions:
#             if i < a or i > b:
#                 continue

# x에서 시작하는 것이 가능한지 판단합니다.
def satisfy(x):
    for a, b in conditions:
        # 계속 2배씩 해주며 
        # a <= x <= b를 항상 만족하는지 확인합니다.
        # 아니라면, False를 반환합니다.
        x *= 2
        if x < a or x > b:
            return False 
    
    return True 


# 가능한 모든 범위에 대해 탐색해봅니다.
# 1 ~ MAX_NUM 사이가 아니라면 애초에 처음부터 불가능합니다.
for x in range(1, MAX_NUM + 1):
    # 만족하는 x가 있다면,
    # 해당 x가 최소이므로 출력합니다. 
    if satisfy(x):
        print(x)
        break 



# for a in range(1, 10):
#     for b in range(1, 10):
#         for c in range(1, 10):
#             if abs(a - 5) != 4 or abs(b - 2) != 4 or abs(c - 3) != 2:
#                 continue
#             if abs(a - 2) != 1 or abs(b - 7) != 1 or abs(c - 6) != 1:
#                 continue

#             print(a, b, c)