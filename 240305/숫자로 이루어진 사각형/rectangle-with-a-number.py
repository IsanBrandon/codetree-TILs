n = int(input())

def print_squre(n):
    num = 1
    for _ in range(n):
        for i in range(n):
            if num == 10:
                num = 1
            print(num, end=" ")
            num += 1
        print()
        
print_squre(n)