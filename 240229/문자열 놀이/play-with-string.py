string, n = tuple(input().split())
int_n = int(n)

for _ in range(int_n):
    type_, w1, w2 = tuple(input().split())
    if type_ == '1':
        arr1 = list(string)
        int_w1, int_w2 = int(w1), int(w2)
        temp = arr1[int_w1-1]
        arr1[int_w1-1] = arr1[int_w2-1]
        arr1[int_w2-1] = temp
        string = ''.join(arr1)
        print(string)
    else:
        arr2 = list(string)
        for i in range(len(arr2)):
            if arr2[i] == w1:
                arr2[i] = w2
        string = ''.join(arr2)
        print(string)