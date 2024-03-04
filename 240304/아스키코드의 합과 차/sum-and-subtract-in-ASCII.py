chr1, chr2 = tuple(map(ord, input().split()))
big = 0
small = 0

if chr1 > chr2:
    big = chr1
    small = chr2
else:
    big = chr2
    small = chr1

print(chr1 + chr2, big - small)