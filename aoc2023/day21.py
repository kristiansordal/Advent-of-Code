from collections import defaultdict

D = open("input/21.in").read()
grid = [[x for x in l] for l in D.splitlines()]
s = D.replace("\n", "").index("S")
s = (s // len(grid[0]), s % len(grid[0]))
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def search(g, s, d):
    q = [s]
    dist = defaultdict(lambda: 2**32)
    dist[s] = 0
    v = set()

    while q:
        r, c = q.pop(0)

        for dr, dc in DIRS:
            rr, cc = r + dr, c + dc

            if g[rr % len(grid)][cc % len(grid[0])] != "#" and (rr, cc) not in v:
                v.add((rr, cc))
                dist[(rr, cc)] = min(dist[(rr, cc)], dist[(r, c)] + 1)
                if dist[(rr, cc)] < d:
                    q.append((rr, cc))
    return dist


step = 26501365
xs = zip([65 + (131 * i) for i in range(0, 3)], [1, 0, 1])
ys = [sum(1 for _, v in search(grid, s, x).items() if v <= x and v % 2 == e) for (x, e) in xs]
n = step // 131

# 1st difference:
a0, a1, a2 = ys

# 2nd difference:
b1, b2 = a1 - a0, a2 - a1

f = lambda n: a0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)
p1 = sum(1 for _, v in search(grid, s, 64).items() if v <= 64 and v % 2 == 0)
p2 = f(n)
print(f"P1: {p1}, P2: {p2}")
