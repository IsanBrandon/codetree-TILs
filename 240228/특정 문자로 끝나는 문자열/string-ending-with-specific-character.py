arr = [
    input()
    for _ in range(10)
]

the_chr = input()

for elem in arr:
    if elem[-1] == the_chr:
        print(elem)
    else:
        print('None')