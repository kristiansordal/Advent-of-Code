D = tuple(open("input/14.in").read().splitlines())
load = lambda d: sum((len(D) - i) * r.count("O") for i, r in enumerate(d))
transpose = lambda d: tuple(map("".join, [*zip(*d)]))
flip = lambda d: tuple(l[::-1] for l in d)
sort = lambda d: tuple(
    "#".join(["".join(sorted(tuple(g), reverse=True)) for g in l.split("#")]) for l in d
)
p1 = p2 = 0
found, grids = set(), []


def cycle():
    global D, p1
    for i in range(1000000000):
        for j in range(4):
            D = flip(sort(transpose(D)))

            if i == 0 and j == 0:
                p1 = load(transpose(flip((D))))

        if D in found:
            first = grids.index(D)
            return load((grids[(1000000000 - first) % (i - first) + first - 1]))
        grids.append(D)
        found.add(D)


p2 = cycle()
print(f"P1: {p1}, P2: {p2}")
