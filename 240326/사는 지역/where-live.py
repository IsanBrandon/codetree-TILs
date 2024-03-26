n = int(input())

class People:
    def __init__(self, name, loc_num, loc_name):
        self.name = name
        self.loc_num = loc_num
        self.loc_name = loc_name

people = []

for _ in range(n):
    name, loc_num, loc_name = tuple(input().split())
    people.append(People(name, loc_num, loc_name))

idx = 0
for i in range(1, n):
    if people[idx].name[0] < people[i].name[0]:
        idx = i

print(f"name {people[idx].name}")
print(f"addr {people[idx].loc_num}")
print(f"city {people[idx].loc_name}")