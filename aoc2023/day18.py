# fmt: off
from re import sub

D = [[*l.split()] for l in open("input/18.in").read().splitlines()]
DIRS = {"D": (1, 0), "U": (-1, 0), "R": (0, 1), "L": (0, -1), 0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

det = lambda x, y: x[0] * y[1] - x[1] * y[0]
r1 = c1 = r2 = c2 = p1 = p2 = 0
v1 = [(r1, c1)]
v2 = [(r2, c2)]

for d, rg, col in D:
    col = sub(r"[\(\)#]", "", col)
    r1, c1 = r1 + DIRS[d][0] * int(rg), c1 + DIRS[d][1] * int(rg)
    r2, c2 = r2 + DIRS[int(col[-1], 16)][0] * int(col[:-1], 16), c2 + DIRS[int(col[-1], 16)][1] * int(col[:-1], 16)
    v1.append((r1, c1))
    v2.append((r2, c2))
    p1 += int(rg)
    p2 += int(col[:-1], 16)


a1 = a2 = 0

for i in range(len(v1) - 1):
    a1 += det(v1[i], v1[i + 1])
    a2 += det(v2[i], v2[i + 1])
a1 += det(v1[-1], v1[0])
a2 += det(v2[-1], v2[0])

p1,p2 = (abs(a1) + p1) // 2 + 1, (abs(a2) + p2) // 2 + 1

print(f"P1: {p1}, P2: {p2}")
