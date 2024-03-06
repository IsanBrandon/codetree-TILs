# a부터 b까지 i를 모두 잡으면서 소수인 것들을 모두 더해준다
# 소수임을 판정해주는함수를 만든다. 

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

a, b = tuple(map(int, input().split()))
ans = 0

for i in range(a, b+1):
    if is_prime(i):
        ans += i

print(ans)