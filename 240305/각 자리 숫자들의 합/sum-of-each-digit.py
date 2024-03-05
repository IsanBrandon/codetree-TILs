n = input()
ans = 0

for elem in n:
    ans += ord(elem) - ord('0')

print(ans)