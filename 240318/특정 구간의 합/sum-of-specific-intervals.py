n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def sum_val(a, b):
    global arr 
    sumsumsum = 0
    for i in range(a-1, b):
        sumsumsum += arr[i]
    return sumsumsum


for _ in range(m):
    a, b = tuple(map(int, input().split()))
    print(sum_val(a, b))