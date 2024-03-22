s_c, m_p, t = tuple(input().split())

class _007:
    def __init__(self, sc, mp, t):
        self.sc = sc
        self.mp = mp
        self.t = t

_007_1 = _007(s_c, m_p, t)

print(f"secret code : {_007_1.sc}")
print(f"meeting point : {_007_1.mp}")
print(f"time : {_007_1.t}")