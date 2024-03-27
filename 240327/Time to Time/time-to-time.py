a, b, c, d = tuple(map(int, input().split()))

min_gap = (c * 60 + d) - (a * 60 + b) 

print(min_gap)