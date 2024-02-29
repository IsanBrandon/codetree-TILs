string = input()

while True:
    if len(string) == 1:
        break
    
    arr = list(string)

    n = int(input())
    
    if n > len(arr):
        arr.pop(len(arr)-1)
    else:
        arr.pop(n)

    string = "".join(arr)
    print(string)