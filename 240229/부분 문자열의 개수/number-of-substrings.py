string = input()
part_str = input()

cnt = 0

for i in range(len(string)-1):
    if string[i] == part_str[0] and string[i + 1] == part_str[1]:
        cnt += 1

print(cnt)