x1, y1, x2, y2 = tuple(map(int, input().split()))
a1, b1, a2, b2 = tuple(map(int, input().split()))

def intersecting(x1, y1, x2, y2, a1, b1, a2, b2):
    if x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1:
        return False 
    else:
        return True 


if intersecting(x1, y1, x2, y2, a1, b1, a2, b2):
    print("overlapping")
else:
    print("nonoverlapping")