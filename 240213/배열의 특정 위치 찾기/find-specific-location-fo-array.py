arr = list(map(int, input().split()))
even_sum = 0
multi_3_sum = 0
multi_3_cnt = 0

for elem in arr:
    if elem % 2 == 0:
        even_sum += elem
    if elem % 3 == 0:
        multi_3_sum += elem
        multi_3_cnt += 1

avg_3 = multi_3_sum / multi_3_cnt

print(f"{even_sum} {avg_3 :1.f}")