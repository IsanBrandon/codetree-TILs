n = int(input())
arr = list(map(int, input().split()))


def seletion_sort():
    # size = len(arr)

    for i in range(n - 1):
        minimum = i
        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum = j 
        # tmp = arr[i]
        # arr[i] = arr[minimum]
        # arr[minimum] = tmp
        arr[i], arr[minimum] = arr[minimum], arr[i]
    
    # return arr


seletion_sort()

for elem in arr:
    print(elem, end=" ")