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

print(f"name {people[n-1].name}")
print(f"addr {people[n-1].loc_num}")
print(f"city {people[n-1].loc_name}")