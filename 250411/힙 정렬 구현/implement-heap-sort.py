n = int(input())
arr = [0] + list(map(int, input().split()))

# Please write your code here.
def heapity(n, i):
    largest = i
    l = i * 2
    r = i * 2 + 1

    if l <= n and arr[l] > arr[largest]:
        largest = l
    
    if r <= n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapity(n, largest)

def heap_sort():
    for i in range(n // 2, 0, -1):
        heapity(n, i)

    for i in range(n, 1, -1):
        arr[l], arr[i] = arr[i], arr[l]
        heapity(i - 1, 1)