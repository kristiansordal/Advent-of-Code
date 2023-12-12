import numpy as np


def search(grid, r, c):
    file = open("input/10_vis.txt", "w")
    visited = {(r, c)}
    q = [(r, c)]
    chars = {"|": "┃", "-": "━", "L": "┗", "J": "┛", "7": "┓", "F": "┏", "S": "S"}

    while q:
        r, c = q.pop()
        tile = grid[r][c]

        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            continue

        if tile in "S|JL" and grid[r - 1][c] in "|7F" and (r - 1, c) not in visited:
            visited.add((r - 1, c))
            q.append((r - 1, c))

        # Right move
        if tile in "S|7F" and grid[r + 1][c] in "|JL" and (r + 1, c) not in visited:
            visited.add((r + 1, c))
            q.append((r + 1, c))

        # Up move
        if tile in "S-J7" and grid[r][c - 1] in "-LF" and (r, c - 1) not in visited:
            visited.add((r, c - 1))
            q.append((r, c - 1))

        # Down move
        if tile in "S-LF" and grid[r][c + 1] in "-J7" and (r, c + 1) not in visited:
            visited.add((r, c + 1))
            q.append((r, c + 1))

    for i, r in enumerate(grid):
        s = ""
        for j, c in enumerate(r):
            if (i, j) in visited:
                s += chars[c]
            else:
                s += "."
        file.write(s + "\n")
    file.close()

    return visited


def inside(grid, visited):
    bitmap = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    file = open("input/10_bitmap.txt", "w")

    print(list(sorted(list(visited))))

    for r in range(len(grid)):
        b = 0
        s = ""
        for c in range(len(grid[0])):
            if (r, c) in visited:
                b |= 1 << c
                s += "#"
            else:
                s += "."

        file.write(s + "\n")
    file.close()


def main():
    D = open("input/10.in").read()
    grid = D.splitlines()
    start = D.replace("\n", "").index("S")
    r, c = start // len(grid[0]), start % len(grid[0])
    visited = search(grid, r, c)
    inside(grid, visited)


if __name__ == "__main__":
    main()
