# arr.sort()
# arr.sort(reverse=True)
# arr = sorted(arr)
# arr = arr[::-1]
# arr = list(reversed(arr))

n = int(input())
arr = list(map(int, input().split()))

# MINE
# s_arr = sorted(arr)
# r_arr = list(reversed(s_arr))

# for elem in s_arr:
#     print(elem, end=" ")
# print()
# for elem in r_arr:
#     print(elem, end=" ")

# CODETREE
# 오름차순 정렬
arr.sort()

for elem in arr:
    print(elem, end=" ")
print()

# 내림차순 정렬
arr.sort(reverse=True)

for elem in arr:
    print(elem, end=" ")
print()