# fmt: off
from collections import defaultdict
from heapq import heappop, heappush

D = [[int(x) for x in l] for l in open("input/17.in").read().splitlines()]

def search(mi, mx):
    v = set()
    dist = defaultdict(lambda: 2**32)
    dist[(0, 0, (0, 0))] = 0
    q: list[tuple] = [(0, 0, 0, (0, 0))]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        w, r, c, dir = heappop(q)

        if (r, c) == (len(D) - 1, len(D[0]) - 1): return w
        if (r, c, dir) in v: continue

        v.add((r, c, dir))
        for dr, dc in dirs:
            if (dr, dc) == dir or (dr * -1, dc * -1) == dir: continue

            nw = 0
            for i in range(1, mx + 1):
                nr, nc = r + dr * i, c + dc * i

                if 0 <= nr < len(D) and 0 <= nc < len(D[0]):
                    nw += D[nr][nc]

                    if i < mi: continue

                    if dist[(nr, nc, (dr, dc))] > w + nw:
                        dist[(nr, nc, (dr, dc))] = w + nw
                        heappush(q, (w + nw, nr, nc, (dr, dc)))


p1,p2 = search(1, 3),search(4, 10)
print(f"P1: {p1}, P2: {p2}")
