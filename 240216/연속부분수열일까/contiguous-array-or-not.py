import sys

n1 , n2 = tuple(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(n1):
    
    success = True

    for j in range(n2):

        if i + j >= n1:
            success = False
            break 

        if arr1[i + j] != arr2[j]:
            success = False
            break 

    if success:
        print("Yes")
        sys.exit()

print("No")