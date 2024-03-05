n = int(input())
sum_val = 0

for _ in range(n):
    elem = int(input())
    sum_val += elem

sum_val = str(sum_val)
string = ""
string = sum_val[1:] + sum_val[0]
print(string)