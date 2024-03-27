m1, d1, m2, d2 = tuple(map(int, input().split()))

### MINE ###
# month, day = m1, d1
# elapsed_days = 0

# #                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
# num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# while True:
#     if month == m2 and day == d2:
#         break
    
#     elapsed_days += 1
#     day += 1

#     if day > num_of_days[month]:
#         month += 1
#         day = 1

# print(elapsed_days + 1)

### CODETREE ###
def num_of_days(m, d):
    # 계산 편의 상 월마다 몇 일이 있는지 적어주기
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    # 1월부터 (m - 1)월 까지는 전부 꽉 채워져 있습니다.
    for i in range(1, m):
        total_days += days[i]

    # m월의 경우에는 정확히 d일만 있습니다.
    total_days += d
    return total_days

total_days = num_of_days(m2, d2) - num_of_days(m1, d1) + 1
print(total_days)