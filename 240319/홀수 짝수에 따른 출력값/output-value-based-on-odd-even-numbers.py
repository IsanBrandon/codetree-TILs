n = int(input())

def get_sum(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    # n과 홀짝이 같은 수만을 재귀함수로 호출합니다.
    return get_sum(n - 2) + n

print(get_sum(n))