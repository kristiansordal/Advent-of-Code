D = [[*x.split()] for x in open("input/2.in").read().splitlines()]
h = d1 = d2 = a = 0
for [c, x] in D:
    if c[0] == "f":
        h += int(x)
        d2 += int(x) * a
    if c[0] == "u":
        d1 -= int(x)
        a -= int(x)
    if c[0] == "d":
        d1 += int(x)
        a += int(x)
p1 = h * d1
p2 = h * d2

print(f"P1: {p1}, P2: {p2})")
