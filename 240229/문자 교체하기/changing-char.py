str1, str2 = tuple(input().split())

arr1 = list(str1)
arr2 = list(str2)

arr2[0], arr2[1] = arr1[0], arr1[1]

str2 = ''.join(arr2)

print(str2)