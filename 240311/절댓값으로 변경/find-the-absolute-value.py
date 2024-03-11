n = int(input())
arr = list(map(int, input().split()))

def absolute_value(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] *= -1
    return arr

for elem in absolute_value(arr):
    print(elem, end=" ")