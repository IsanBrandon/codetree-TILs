arr = list(map(int, input().split()))
even_sum = 0
odd_sum = 0

for elem in arr:
    if elem % 2 == 0:
        even_sum += elem
    else:
        odd_sum += elem

if even_sum >= odd_sum:
    print(even_sum - odd_sum)
else:
    print(odd_sum - even_sum)