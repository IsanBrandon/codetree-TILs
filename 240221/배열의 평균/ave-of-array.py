arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

# 가로 평균
for i in range(2):
    sum_val = 0
    for j in range(4):
        sum_val += arr_2d[i][j]
    sum_avg = sum_val / 4
    print(f"{sum_avg:.1f}", end=" ")
print()

# 세로 평균 & 전체 평균
column_1st = 0
column_2nd = 0
column_3rd = 0
column_4th = 0
for i in range(2):
    for j in range(4):
        if j == 0:
            column_1st += arr_2d[i][j]
        elif j == 1:
            column_2nd += arr_2d[i][j]
        elif j == 2:
            column_3rd += arr_2d[i][j]
        else:
            column_4th += arr_2d[i][j]
c1 = column_1st / 2
c2 = column_2nd / 2
c3 = column_3rd / 2
c4 = column_4th / 2
print(f"{c1:.1f} {c2:.1f} {c3:.1f} {c4:.1f}")
print(f"{(column_1st + column_2nd + column_3rd + column_4th) / 8:.1f}")