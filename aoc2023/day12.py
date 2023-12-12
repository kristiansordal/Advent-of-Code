from functools import cache


@cache
def combs(s, g, sz=0):
    if not s:
        return 1 if (len(g) == 1 and g[0] == sz) or (len(g) == 0 and sz == 0) else 0

    if s[0] == ".":
        return combs(s[1:], g) if sz == 0 else (combs(s[1:], g[1:]) if sz == g[0] else 0)

    if s[0] == "?":
        return combs("." + s[1:], g, sz) + combs("#" + s[1:], g, sz)

    if s[0] == "#":
        return 0 if not g or sz > g[0] else combs(s[1:], g, sz + 1)

    return 0


D = open("input/12.in").read().splitlines()
s1, g1 = [l.split()[0] for l in D], [tuple(int(x) for x in l.split()[1].split(",")) for l in D]
s2, g2 = [(l.split()[0] + "?") * 5 for l in D], [
    tuple(int(x) for x in l.split()[1].split(",") * 5) for l in D
]
p1 = sum(combs(s, g) for s, g in zip(s1, g1))
p2 = sum(combs(s[:-1], g) for s, g in zip(s2, g2))

print(f"P1: {p1}, P2: {p2}")
