D = [l.splitlines() for l in open("input/13.in").read().split("\n\n")]


def matching(r, s):
    for i in range(1, len(r)):
        if (
            sum(sum(c1 != c2 for c1, c2 in zip(r1, r2)) for r1, r2 in zip(r[i - 1 :: -1], r[i:]))
            == s
        ):
            return i
    return -1


p1 = p2 = 0
for s in 0, 1:
    sm = 0
    for r in D:
        cols = matching(r, s)
        rows = matching([*zip(*r)], s)
        if cols > 0:
            sm += cols * 100
        if rows > 0:
            sm += rows
    if s == 0:
        p1 = sm
    else:
        p2 = sm

print(f"P1 {p1}, P2 {p2}")
