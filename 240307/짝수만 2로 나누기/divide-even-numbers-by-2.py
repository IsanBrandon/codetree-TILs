n = int(input())
_list = list(map(int, input().split()))

def if_even_div_2(arr):
    leng = len(arr)
    for i in range(leng):
        if arr[i] % 2 == 0:
            arr[i] //= 2
        else:
            pass
    return arr

_list = if_even_div_2(_list)

for elem in _list:
    print(elem, end=" ")