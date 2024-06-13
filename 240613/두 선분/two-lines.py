a, b, c, d = tuple(map(int, input().split()))
# check = [0] * 101

def intersecting(a, b, c, d):
    # 겹치지 않는 경우에 대한 처리를 먼저 진행합니다. 
    if b < c or d < a:
        return False
    # 나머지는 전부 겹치는 경우라고 볼 수 있습니다.
    else:
        return True 

if intersecting(a, b, c, d):
    print("nonintersecting")
else:
    print("intersecting")


# for i in range(a, b + 1):
#     check[i] += 1

# for j in range(c, d + 1):
#     check[j] += 1

# ans = False

# for finding in check:    
#     if finding >= 2:
#         ans = True

# if ans:
#     print("intersecting")
# else:
#     print("nonintersecting")