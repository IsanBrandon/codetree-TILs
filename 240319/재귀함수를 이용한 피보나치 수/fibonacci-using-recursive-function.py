n = int(input())

def Fibo(n):
    if n <= 2:
        return 1 
    
    return Fibo(n-1) + Fibo(n-2)

print(Fibo(n))