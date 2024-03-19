n = int(input())

def sum_12N(n):
    if n == 1:
        return 1
    
    return sum_12N(n-1) + n

print(sum_12N(n))