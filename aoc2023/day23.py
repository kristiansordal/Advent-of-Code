import sys
from collections import defaultdict
import networkx as nx

sys.setrecursionlimit(100000)
D = open("input/23.in").read().splitlines()
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dist = defaultdict(lambda: 0)
v = set()
dg = nx.DiGraph()
pred = defaultdict(tuple)
pred[(0, 1)] = (0, 1)


def longestpath(g, r, c):
    if (r, c) == (0, 1):
        return 0

    v.add((r, c))

    if (r, c) in dist.keys():
        return dist[(r, c)]

    ml = 0
    for dr, dc in DIRS:
        rr, cc = r + dr, c + dc

        if 0 <= rr < len(g) and 0 <= cc < len(g[0]) and (rr, cc) not in v:
            if g[rr][cc] != "#":
                # if g[rr][cc] == ">" and c < cc:
                #     continue
                # if g[rr][cc] == "<" and c > cc:
                #     continue
                # if g[rr][cc] == "v" and r < rr:
                #     continue
                # if g[rr][cc] == "^" and r > rr:
                #     continue

                l = longestpath(g, rr, cc)
                ml = max(ml, l)

    v.discard((r, c))
    dist[(r, c)] = ml + 1
    return dist[(r, c)]


for e1, e2 in dg.edges:
    print(e1, e2, dg.get_edge_data(e1, e2))
p1 = longestpath(D, len(D) - 1, len(D[0]) - 2)
print(p1)
