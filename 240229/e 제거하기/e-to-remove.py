string = input()
arr = list(string)

for i in range(len(arr)):
    if arr[i] == 'e':
        arr.pop(i)
        break

string = "".join(arr)
print(string)