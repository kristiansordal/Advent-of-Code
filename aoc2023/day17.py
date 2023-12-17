from heapq import heapify, heappop, heappush

D = [[int(x) for x in l] for l in open("input/17.in").read().splitlines()]


def search(mi, mx):
    s = (0, 0)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    d, v, q = {s: 0}, set(), [(0, s, (0, 0), 1)]
    heapify(q)
    g = [["." for _ in range(len(D[0]))] for _ in range(len(D))]
    pred = {s: None}
    for i, r in enumerate(D):
        for j, c in enumerate(r):
            if (i, j) != (0, 0):
                d[(i, j)] = 2**32  # pyright: ignore[reportGeneralTypeIssues]
                heappush(q, (2**32, (i, j), (0, 0), 0))  # pyright: ignore[reportGeneralTypeIssues]

    while q:
        w, (r, c), dir, cnt = heappop(q)

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if 0 <= nr < len(D) and 0 <= nc < len(D[0]) and (nr, nc) not in v:
                v.add((nr, nc))

                if d[(nr, nc)] > w + D[nr][nc]:
                    pred[(nr, nc)] = (r, c)
                    if (dr, dc) != dir:
                        d[(nr, nc)] = w + D[nr][nc]
                        heappush(q, (w + D[nr][nc], (nr, nc), (dr, dc), 0))
                    elif (dr, dc) == dir and cnt < mx:
                        d[(nr, nc)] = w + D[nr][nc]
                        heappush(q, (w + D[nr][nc], (nr, nc), dir, cnt + 1))

    # p = (len(D) - 1, len(D[0]) - 1)
    # while p is not None:
    #     g[p[0]][p[1]] = "#"
    #     p = pred[p]
    # with open("path.txt", "w") as f:
    #     for r in g:
    #         f.write("".join(r) + "\n")

    return d[(len(D) - 1, len(D[0]) - 1)]


# p1 = search(0, 3)
p2 = search(4, 10)
# print(p1)
# print(p2)

# print(d[(len(D) - 1, len(D[0]) - 1)])
