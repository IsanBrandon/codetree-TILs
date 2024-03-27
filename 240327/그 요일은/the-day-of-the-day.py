MONTHS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
WEEKEND = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = map(int, input().split())
week = input()

days = MONTHS[m1] - d1 + 1 + sum(MONTHS[m1+1:m2]) + d2 if m1 != m2 else d2 - d1 + 1
# print(days)
# print(days//7, days%7)


if WEEKEND.index(week)+1 <= (days % 7) and days > 7:
    # print("y")
    print(days//7 + 1)
elif days<7:
  if WEEKEND.index(week)+1 <= (days % 7):
    print(1)
else:
    print(days//7)