strA = input()
strB = input()

AB = "".join([strA, strB])
BA = "".join([strB, strA])

if AB == BA:
    print("true")
else:
    print("false")