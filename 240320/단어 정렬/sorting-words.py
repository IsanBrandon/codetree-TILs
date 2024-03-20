n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

arr = sorted(arr)
for elem in arr:
    print(elem)