# type: ignore
D = open("input/20.in").read().splitlines()
from math import lcm

LO, HI, ON, OFF, FLIPFLOP, CONJUNCTION = 0, 1, 1, 0, "%", "&"


class Module:
    def __init__(self, name, typ, output):
        self.name = name
        self.typ = typ
        self.output = output

        if typ == FLIPFLOP:
            self.memory = OFF
        else:
            self.memory = {}


bcast = []
modules = {}

for d in D:
    f, t = d.strip().split(" -> ")
    t = t.split(", ")

    if f == "broadcaster":
        bcast = t
    else:
        typ = f[0]
        name = f[1:]
        modules[name] = Module(name, typ, t)

for n, m in modules.items():
    for o in m.output:
        if o in modules and modules[o].typ == CONJUNCTION:
            modules[o].memory[n] = LO

(feed,) = [n for n, m in modules.items() if "rx" in m.output]
CYCLES = {}
SEEN = {n: 0 for n, m in modules.items() if feed in m.output}
lo, hi, ps = 0, 0, 0
p1, p2 = 0, 0

while True:
    lo += 1
    ps += 1
    q = [("broadcaster", x, LO) for x in bcast]

    while q:
        f, t, p = q.pop(0)

        if p == LO:
            lo += 1
        else:
            hi += 1

        if ps == 1000:
            p1 = lo * hi

        if t not in modules:
            continue

        m = modules[t]

        if m.name == feed and p == HI:
            SEEN[f] += 1

            if f not in CYCLES:
                CYCLES[f] = ps

            if all(SEEN.values()):
                p2 = lcm(*CYCLES.values())
                print(f"P1: {p1}, P2: {p2}")
                exit()

        if m.typ == FLIPFLOP:
            if p == LO:
                m.memory = ON if not m.memory else OFF
                out = HI if m.memory else LO
                for n in m.output:
                    q.append((m.name, n, out))
        else:
            m.memory[f] = p
            out = LO if all(x for x in m.memory.values()) else HI
            for n in m.output:
                q.append((m.name, n, out))
