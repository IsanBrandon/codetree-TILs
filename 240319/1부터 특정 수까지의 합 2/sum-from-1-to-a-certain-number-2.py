n = int(input())

def sum_12N(n):
    if n == 0:
        return 0
    
    return sum_12N(n-1) + n

print(sum_12N(n))