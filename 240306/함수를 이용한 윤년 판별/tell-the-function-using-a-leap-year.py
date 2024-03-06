def special_year(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
    if y % 4 == 0:
        return True
    return False

year = int(input())

if special_year(year):
    print("true")
else:
    print("false")