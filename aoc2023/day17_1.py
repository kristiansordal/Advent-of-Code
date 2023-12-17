# fmt : off
from heapq import heapify, heappop, heappush


class Node:
    def __init__(self, r, c, w, d, cnt):
        self.r = r
        self.c = c
        self.w = w
        self.d = d
        self.cnt = cnt

    def coords(self):
        return (self.r, self.c)

    def __eq__(self, o):
        return self.w == o.w

    def __lt__(self, o):
        return self.w < o.w

    def __str__(self):
        return f"Coords: ({self.r},{self.c})\nWeight: {self.w}\nDir: {self.d}"


D = [[int(x) for x in l] for l in open("input/17.in").read().splitlines()]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def search(mi, mx) -> int:
    s = Node(0, 0, 0, (0, 0), 0)
    d = {s.coords(): 0}
    q = [s]
    v = set()
    heapify(q)
    p = {s.coords(): None}
    g = [["." for _ in range(len(D[0]))] for _ in range(len(D))]

    while q:
        n = heappop(q)

        if n.coords() in v:  # Skip if already processed with a lower cost
            continue

        v.add(n.coords())

        for dr, dc in dirs:
            nr, nc = n.r + dr, n.c + dc

            if 0 <= nr < len(D) and 0 <= nc < len(D[0]):
                w = D[nr][nc]

                if (nr, nc) not in d or w + d[n.coords()] < d[(nr, nc)]:
                    d[(nr, nc)] = w + d[n.coords()]
                    cnt = n.cnt + 1 if (dr, dc) == n.d else 0

                    if (dr, dc) != n.d or cnt <= mx:
                        heappush(q, Node(nr, nc, w + d[n.coords()], (dr, dc), cnt))
                        p[(nr, nc)] = n.coords()  # pyright: ignore[reportGeneralTypeIssues]

    return d[(len(D) - 1, len(D[0]) - 1)]


p1 = search(0, 3)
print(p1)
