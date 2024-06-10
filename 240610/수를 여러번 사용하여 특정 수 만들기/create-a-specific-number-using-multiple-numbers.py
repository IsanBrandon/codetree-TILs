a, b, c = tuple(map(int, input().split()))
temp_a, temp_b = a, b

max_num = 0
for i in range(1000):
    a *= i
    for j in range(1000):
        sum_num = 0
        b *= j

        if a + b > c:
            break 
        else:
            sum_num = a + b
    
        max_num = max(max_num, sum_num)
        if j == 0:
            b = temp_b
        else:
            b //= j 

    if i == 0:
        a = temp_a
    else:
        a //= i

print(max_num)