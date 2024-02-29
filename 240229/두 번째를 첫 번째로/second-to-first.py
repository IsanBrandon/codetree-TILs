string = input()
first_word = string[0]
second_word = string[1]

arr = list(string)

for i in range(len(arr)):
    if arr[i] == second_word:
        arr[i] = first_word

string = "".join(arr)
print(string)