n = int(input())
arr = list(map(int, input().split()))


def insertion_sort():
    for i in range(n):
        j = i - 1
        key = arr[i]
        while (j >= 0 & arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


for elem in arr:
    print(elem, end=" ")