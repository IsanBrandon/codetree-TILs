class Agents:
    def __init__(self, name, score):
        self.name = name
        self.score = score

agents = [
    tuple(map(int, input().split()))
    for _ in range(5)
]

agent1 = Agents[0]
agent2 = Agents[1]
agent3 = Agents[2]
agent4 = Agents[3]
agent5 = Agents[4]

for i in range(5):