n = int(input())
arr = list(map(int, input().split()))


def seletion_sort(arr):
    size = len(arr)

    for i in range(size - 1):
        minimum = i
        for j in range(i+1, size):
            if arr[j] < arr[minimum]:
                minimum = j 
        tmp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = tmp
    
    return arr


seletion_sort(arr)

for elem in arr:
    print(elem, end=" ")