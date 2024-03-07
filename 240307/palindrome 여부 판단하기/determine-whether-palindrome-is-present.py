arr = input()

def is_palindrome(arr):
    leng = len(arr)
    for i in range(leng):
        if arr[i] != arr[leng-1-i]:
            return False
    return True

if is_palindrome(arr):
    print("Yes")
else:
    print("No")