y, m, d = tuple(map(int, input().split()))
#################################################################        
# 윤년인지 확인
def is_leap_year(y):
    if y % 4 != 0:
        return False
    if y % 100 != 0:
        return True
    if y % 400 == 0:
        return True
    return False
#################################################################        
# 윤년일 때 존재여부 체크
def leaf_last_day_number(m):
    if m == 2:
        return 29
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    return 31

def leaf_judge_day(m, d):
    if m <= 12 and d <= leaf_last_day_number(m):
        return True 
    else:
        return False

# 윤년 아닐 때 존재여부 체크 
def not_leaf_last_day_number(m):
    if m == 2:
        return 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    return 31

def not_leaf_judge_day(m, d):
    if m <= 12 and d <= not_leaf_last_day_number(m):
        return True 
    else:
        return False
#################################################################
# 존재하는 날인지 확인해주기
def is_exist_day(y, m, d):
    if is_leap_year(y):
        if leaf_judge_day(m, d):
            return True
        else:
            return False
    else:
        if not_leaf_judge_day(m, d):
            return True
        else:
            return False
#################################################################
# 존재하는 날이라면 계절을 뽑아주기
def that_day_the_season(m):
    if m >= 3 and m <= 5:
        return "Spring"
    elif m >= 6 and m <= 8:
        return "Summer"
    elif m >= 9 and m <= 11:
        return "Fall"
    else:
        return "Winter"
#################################################################
# Main{}
if is_exist_day(y, m, d):
    print(that_day_the_season(m))
else:
    print("-1")