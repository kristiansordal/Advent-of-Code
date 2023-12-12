import numpy as np
from itertools import combinations

D = np.array([[c for c in l] for l in open("input/11.in").read().splitlines()])
rid = set(i for i, l in enumerate(D) if "#" not in l)
cid = set(i for i, l in enumerate(zip(*D)) if "#" not in l)
ids = combinations((zip(*np.where(D == "#"))), 2)
p1, p2 = 0, 0

for (r1, c1), (r2, c2) in ids:
    rc = len([x for x in rid if min(r1, r2) < x < max(r1, r2)])
    cc = len([x for x in cid if min(c1, c2) < x < max(c1, c2)])
    p1 += abs(r1 - r2) + abs(c1 - c2) - rc - cc + rc * 2 + cc * 2
    p2 += abs(r1 - r2) + abs(c1 - c2) + rc * 999999 + cc * 999999

print(f"P1: {p1}, P2: {p2}")
