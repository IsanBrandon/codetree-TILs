string = input()

arr = list(string)
first = arr[0]
second = arr[1]

for i in range(len(arr)):
    if arr[i] == first:
        arr[i] = second
    elif arr[i] == second:
        arr[i] = first

string = ''.join(arr)
print(string)