arr = [
    input()
    for _ in range(10)
]

the_chr = input()
exsist = False

for elem in arr:
    if elem[-1] == the_chr:
        print(elem)
        exsist = True
        
if exsist == False:
    print('None')