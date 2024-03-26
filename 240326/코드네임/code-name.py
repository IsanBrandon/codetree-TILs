# 클래스 선언
class Agents:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score

# 변수 선언 및 입력
agents = []

for _ in range(5):
    code_name, score = tuple(input().split())
    agents.append[Agents(code_name, int(score))]

# 최소 점수를 갖는 유저 찾기
min_idx = 0 
for i in range(1, 5):
    if agents[min_idx].score > agents[i].score:
        min_idx = i

# 출력
print(agents[min_idx].code_name, agents[min_idx].score)