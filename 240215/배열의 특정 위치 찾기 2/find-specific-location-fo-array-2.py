arr = list(map(int, input().split()))
even_sum = 0
odd_sum = 0

for i in range(len(arr)):
    if i % 2 == 0:
        even_sum += arr[i]
    else:
        odd_sum += arr[i]

if even_sum >= odd_sum:
    print(even_sum - odd_sum)
else:
    print(odd_sum - even_sum)