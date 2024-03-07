n_M, n_D = tuple(map(int, input().split()))

def date_exsist(M, D):
    if M == 2 and D <= 28:
        return True
    elif M <= 7 and M % 2 != 0 and D <= 31:
        return True
    elif M <= 7 and M % 2 == 0 and D <= 30:
        return True
    elif M >= 8 and M % 2 == 0 and D <= 31:
        return True
    elif M >= 8 and M % 2 != 0 and D <= 30:
        return True
    else:
        return False

if date_exsist(n_M, n_D):
    print("Yes")
else:
    print("No")