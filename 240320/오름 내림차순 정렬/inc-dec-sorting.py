# arr.sort()
# arr.sort(reverse=True)
# arr = sorted(arr)
# arr = arr[::-1]
# arr = list(reversed(arr))

n = int(input())
arr = list(map(int, input().split()))

s_arr = sorted(arr)
r_arr = list(reversed(s_arr))

print(s_arr)
print(r_arr)