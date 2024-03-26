class People:
    def __init__(self, name, loc_num, loc_name):
        self.name = name
        self.loc_num = loc_num
        self.loc_name = loc_name

# 변수 선언 및 입력
n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
people = [People(name, loc_num, loc_name) for name, loc_num, loc_name in arr]
# for _ in range(n):
#     name, loc_num, loc_name = tuple(input().split())
#     people.append(People(name, loc_num, loc_name))

# 사전순으로 이름이 가장 느린 사람 찾기
target_idx = 0
for i, person in enumerate(people):
#    if people[idx].name[0] < people[i].name[0]:
#        idx = i
    if person.name > people[target_idx].name:
        target_idx = i

print(f"name {people[target_idx].name}")
print(f"addr {people[target_idx].loc_num}")
print(f"city {people[target_idx].loc_name}")