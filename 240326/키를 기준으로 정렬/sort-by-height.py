class People:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

n = int(input())
# arr = [tuple(input().split()) for _ in range(n)]
# people = [People(name, height, weight) for name, height, weight in arr]
people = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    people.append(People(name, int(height), int(weight)))

people.sort(key=lambda x: x.height)

for person in people:
    print(person.name, person.height, person.weight)