cnt = 0
given_str = []
while True:
    string = input()
    given_str.append(string)
    if string == '0':
        print(cnt)
        break
    cnt += 1
    
for i in range(1, cnt+1):
    if i % 2 == 1:
        print(given_str[i-1])