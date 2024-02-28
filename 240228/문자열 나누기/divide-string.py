n = int(input())

tot_str = ""
string = input().split()
for elem in string:
    tot_str += elem

cnt = 1

for elem in tot_str:
    if cnt <= 5: 
        print(elem, end="")
        cnt += 1
    else:
        print()
        print(elem, end="")
        cnt = 2