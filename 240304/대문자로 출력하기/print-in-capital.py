string = input()

# 문자를 하나하나 확인하여 알파벳일 경우 모두 대문자로 출력합니다.
for elem in string:
    if (elem >= 'A' and elem <= 'Z') or (elem >= 'a' and elem <= 'z'):
        print(elem.upper(), end="")