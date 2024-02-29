string = input()
target = input()

leng = len(string)
start_idx = -1

for i in range(leng-1):
    if string[i] == target[0] and string[i+1] == target[1]:
        start_idx = i
        break

print(start_idx)