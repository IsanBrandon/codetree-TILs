n = int(input())
arr = []

    


for _ in range(n):
    input_str = input()
    
    if input_str.startswith('push_back'):
        _, integer = input_str.split()
        arr.append(int(integer))
        
    elif input_str.startswith('pop_back'):
        arr.pop()

    elif input_str.startswith('size'):
        print(len(arr))
    
    else:
        _, num = input_str.split()
        print(arr[int(num) - 1])