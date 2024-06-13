a, b, c, d = tuple(map(int, input().split()))
check = [0] * 101


if b < c or d < a:
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