from itertools import cycle

D = [int(x) for x in open("input/1.in").read().splitlines()]
p1, p2 = sum(D), 0
s, l = 0, set()
for d in cycle(D):
    s += d
    if s in l:
        p2 = s
        break
    l.add(s)


print(f"P1: {p1}, P2: {p2}")
