# MINE
n = int(input())
# arr = []

# for _ in range(n):
#     arr.append(input())

# arr = sorted(arr)
# for elem in arr:
#     print(elem)

# CODETREE
word_list = [
    input()
    for _ in range(n)
]

word_list.sort()

for word in word_list:
    print(word)