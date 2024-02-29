string, n = tuple(input().split())
int_n = int(n)

for _ in range(int_n):
    type_, w1, w2 = tuple(input().split())
    if type_ == '1':
        modified1 = string
        arr1 = list(modified1)
        int_w1, int_w2 = int(w1), int(w2)
        temp = arr1[int_w1-1]
        arr1[int_w1-1] = arr1[int_w2-1]
        arr1[int_w2-1] = temp
        modified1 = ''.join(arr1)
        print(modified1)
    else:
        modified2 = string
        arr2 = list(modified2)
        for i in range(len(arr2)):
            if arr2[i] == w1:
                arr2[i] = w2
        modified2 = ''.join(arr2)
        print(modified2)