# fmt: off
# type: ignore
from collections import defaultdict
import networkx as nx
import sys

sys.setrecursionlimit(1000000)
D = open("input/23.in").read().splitlines()
DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dist = defaultdict(lambda: 0)
v = set()

for i in range(len(D)):
    for j in range(len(D[0])):
        n = 0
        for dr, dc in DIRS:
            rr, cc = i + dr, j + dc
            if 0 <= rr < len(D) and 0 <= cc < len(D[0]) and D[rr][cc] != "#":
                n += 1
            if n > 2 and D[i][j] != "#":
                v.add((i, j))

    v.add((0, 1))
    v.add((len(D) - 1, len(D[0]) - 2))


def init_graph(r, c, slopes=True):
    g = nx.Graph() if not slopes else nx.DiGraph()
    g.add_nodes_from(v)

    for r, c in v:
        q = [(r, c, 0)]
        s = set()

        while q:
            rr, cc, d = q.pop()
            if (rr, cc) in s:
                continue

            s.add((rr, cc))

            if (rr, cc) in v and (r, c) != (rr, cc):
                g.add_edge((r, c), (rr, cc), weight=d)
                continue

            for dr, dc in DIRS:
                rr_, cc_ = rr + dr, cc + dc

                if 0 <= rr_ < len(D) and 0 <= cc_ < len(D[0]) and D[rr_][cc_] != "#":
                    if slopes and D[rr_][cc_] == ">" and c > cc_: continue
                    if slopes and D[rr_][cc_] == "<" and c < cc_: continue
                    if slopes and D[rr_][cc_] == "v" and r > rr_: continue
                    if slopes and D[rr_][cc_] == "^" and r < rr_: continue
                    q.append((rr_, cc_, d + 1))
    return g

g1= init_graph(0, 1, True)
g2 = init_graph(0, 1, False)

ans = 0
seen = set()

def dfs(g, s, d):
    global ans
    if s in seen: return
    seen.add(s)

    if s == (len(D) - 1, len(D[0]) - 2): ans = max(ans, d)
    for u in g.neighbors(s):
        if u != (0, 1): dfs(g, u, d + g[s][u]["weight"])

    seen.discard(s)
    return ans


p1 = dfs(g1, (0, 1), 0)
p2 = dfs(g2, (0, 1), 0)

print(f"P1: {p1}, P2: {p2}")
