N = int(input())
arr = list(map(int, input().split()))

fir_max = max(arr)
sec_max = min(arr)

for elem in arr:
    if elem <= fir_max and elem >= sec_max:
        sec_max = elem

print(fir_max, sec_max)