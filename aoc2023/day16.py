D = [[c for c in l] for l in open("input/16.in").read().splitlines()]
RIGHT, LEFT, UP, DOWN = (0, 1), (0, -1), (-1, 0), (1, 0)

def search(r, c, dir):
    visited = set()
    q = [(r, c, dir, set())]

    while q:
        r, c, dir, v = q.pop()
        nr, nc = r + dir[0], c + dir[1]

        if 0 <= nr < len(D) and 0 <= nc < len(D[0]) and (nr, nc) not in v:
            visited.add((nr, nc))
            if D[nr][nc] == ".":
                q.append((nr, nc, dir, v))
                continue

            if dir == RIGHT:
                if D[nr][nc] == "\\": q.append((nr, nc, DOWN, v))
                if D[nr][nc] == "/":  q.append((nr, nc, UP, v))
                if D[nr][nc] == "-":  q.append((nr, nc, dir, v))
                if D[nr][nc] == "|":
                    v.add((nr, nc))
                    q.append((nr, nc, UP, v)); q.append((nr, nc, DOWN, v))

            if dir == LEFT:
                if D[nr][nc] == "\\": q.append((nr, nc, UP, v))
                if D[nr][nc] == "/":  q.append((nr, nc, DOWN, v))
                if D[nr][nc] == "-":  q.append((nr, nc, dir, v))
                if D[nr][nc] == "|":
                    v.add((nr, nc))
                    q.append((nr, nc, UP, v)); q.append((nr, nc, DOWN, v))

            if dir == DOWN:
                if D[nr][nc] == "\\": q.append((nr, nc, RIGHT, v))
                if D[nr][nc] == "/":  q.append((nr, nc, LEFT, v))
                if D[nr][nc] == "|":  q.append((nr, nc, dir, v))
                if D[nr][nc] == "-":
                    v.add((nr, nc))
                    q.append((nr, nc, RIGHT, v)); q.append((nr, nc, LEFT, v))

            if dir == UP:
                if D[nr][nc] == "\\": q.append((nr, nc, LEFT, v))
                if D[nr][nc] == "/":  q.append((nr, nc, RIGHT, v))
                if D[nr][nc] == "|":  q.append((nr, nc, dir, v))
                if D[nr][nc] == "-":
                    v.add((nr, nc))
                    q.append((nr, nc, RIGHT, v)); q.append((nr, nc, LEFT, v))
    return len(visited)


energized = set()
for r in range(len(D)):
    energized.add(search(r-1,0,RIGHT))
    energized.add(search(r-1,len(D[0])-1,LEFT))
for c in range(len(D[0])):
    energized.add(search(0,c-1,DOWN))
    energized.add(search(len(D)-1,c-1,UP))

p1 = search(0, -1, RIGHT)
p2 = max(energized)

print(f"P1: {p1}, P2: {p2}")
