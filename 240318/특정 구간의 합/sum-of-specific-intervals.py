n, m = tuple(map(int, input().split()))
arr = [0] + list(map(int, input().split()))

def sum_val(a, b): 
    return_value = 0
    for i in range(a, b+1):
        return_value += arr[i]

    return return_value


for _ in range(m):
    a, b = tuple(map(int, input().split()))
    print(sum_val(a, b))