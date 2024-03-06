def is_magic_number(n):
    tens = n // 10
    units = n % 10
    sum_val = tens + units 

    if sum_val % 2 == 0 and sum_val % 5 == 0:
        ans = "Yes"
    else:
        ans = "No"
    
    return ans


n = int(input())
print(is_magic_number(n))