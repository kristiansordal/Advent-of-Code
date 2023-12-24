# fmt: off
# type: ignore
from sympy import Symbol, solve_poly_system

class Hailstone:
    def __init__(self, ps, vs):
        self.px, self.py, self.pz = list(ps)
        self.vx, self.vy, self.vz = list(vs)


def intersects(a, b):
    x1, y1, x2, y2 = a.px, a.py, a.px + a.vx, a.py + a.vy
    x3, y3, x4, y4 = b.px, b.py, b.px + b.vx, b.py + b.vy
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if d == 0: return False

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d

    if abs(px - x1) < abs(px - x2) and abs(py - y1) < abs(py - y2): return False
    if abs(px - x3) < abs(px - x4) and abs(py - y3) < abs(py - y4): return False
    return (px, py)


D = [
    [map(int, l.replace(",", " ").split()[0:3]), map(int, l.replace(",", " ").split()[4:])]
    for l in open("input/24.in").read().splitlines()
]

hail = [Hailstone(*d) for d in D]
p1 = 0
crashed = set()


for a in hail:
    for b in hail:
        if a == b: continue
        if (a, b) in crashed or (b, a) in crashed: continue
        if p := intersects(a, b):
            if 200000000000000 <= p[0] <= 400000000000000 and 200000000000000 <= p[1] <= 400000000000000:
                p1 += 1
            crashed.add((a, b))
            crashed.add((b, a))

x, y, z, vx, vy, vz = Symbol("x"), Symbol("y"), Symbol("z"), Symbol("vx"), Symbol("vy"), Symbol("vz")
eqs = []
ts = []

for i, h in enumerate(hail[:3]):
    t = Symbol("t" + str(i))
    ts.append(t)
    eqs += [
        (x + vx * t - h.px - h.vx * t),
        (y + vy * t - h.py - h.vy * t),
        (z + vz * t - h.pz - h.vz * t),
    ]

p2 = solve_poly_system(eqs, *([x, y, z, vx, vy, vz] + ts))
p2 = p2[0][0] + p2[0][1] + p2[0][2]

print(f"P1: {p1}, P2: {p2}")
