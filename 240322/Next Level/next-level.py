class Info:
    def __init__(self, name, lv):
        self.name = name
        self.lv = lv

info1 = Info("codetree", "10")
a, b = tuple(input().split())
info2 = Info(a, b)

print(f"user {info1.name} lv {info1.lv}")
print(f"user {info2.name} lv {info2.lv}")