from heapq import heapify, heappush, heappop
from collections import defaultdict

D = open("input/11.in").read().splitlines()
galaxies = []
grid = [[1 for _ in range(len(D[0]))] for _ in range(len(D))]
for i in range(len(D)):

    # set the row
    if "#" not in D[i]:
        grid[i] = [1000000 if c != "#" else 0 for c in D[i]]

    # set the column
    if "#" not in "".join([row[i] for row in D]):
        for r in range(len(D)):
            grid[r][i] = 1000000

    for j in range(len(D[0])):
        if D[i][j] == "#":
            galaxies.append((i, j))

# for l in grid:
#     print(l)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dists = defaultdict(list)
pairs = set()

for galaxy in galaxies:
    q = [(0, galaxy)]
    dist = defaultdict(lambda: 2**32)
    dist[galaxy] = 0
    visited = {galaxy}
    heapify(q)

    while q:
        d, (r, c) = heappop(q)

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
                continue

            if (nr, nc) not in visited:
                visited.add((nr, nc))

                if dist[(nr, nc)] > grid[nr][nc] + d:
                    dist[(nr, nc)] = grid[nr][nc] + d
                    heappush(q, (dist[(nr, nc)], (nr, nc)))

                    if (
                        (nr, nc) in galaxies
                        and ((nr, nc), galaxy) not in pairs
                        and (nr, nc) != galaxy
                    ):
                        dists[galaxy].append(((nr, nc), dist[(nr, nc)]))
                        pairs.add((galaxy, (nr, nc)))
p1 = 0
x = 0
paths = []
for k, l in dists.items():
    paths.append(len(l))
    for (x, y), i in l:
        p1 += i
        x += 1
print(p1, x)
