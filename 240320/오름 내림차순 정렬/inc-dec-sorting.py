# arr.sort()
# arr.sort(reverse=True)
# arr = sorted(arr)
# arr = arr[::-1]
# arr = list(reversed(arr))

n = int(input())
arr = list(map(int, input().split()))

s_arr = sorted(arr)
r_arr = list(reversed(s_arr))

for elem in s_arr:
    print(elem, end=" ")
print()
for elem in r_arr:
    print(elem, end=" ")