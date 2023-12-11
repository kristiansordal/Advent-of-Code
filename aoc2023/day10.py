import numpy as np


def search(grid, r, c):
    visited = {(r, c)}
    q = [(r, c)]

    while q:
        r, c = q.pop()
        tile = grid[r][c]

        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            continue

        # Left move
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

    return visited


def inside(grid, visited):
    bitmap = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    print(visited)
    for r in range(len(grid)):
        s = 0
        for c in range(len(grid[0]) - 1):
            if (r, c) not in visited and (r, c + 1) in visited:
                bitmap[r][c] = s % 2 == 0
                print(s)
            elif (r, c + 1) in visited and (r, c) not in visited:
                bitmap[r][c] = s % 2 == 0
                s += 1
                print(s)
            else:
                bitmap[r][c] = s % 2 == 0

    for c in range(len(grid[0]) - 1):
        s = 0
        for r in range(len(grid)):
            # if grid[r][c] == "." and (r, c + 1) in visited:
            if (r, c) not in visited and (r, c + 1) in visited:
                bitmap[r][c] &= s % 2 == 0
                print(bitmap[r][c])
            # elif (r, c) in visited and grid[r][c + 1] == ".":
            elif (r, c + 1) in visited and (r, c) not in visited:
                bitmap[r][c] &= s % 2 == 0
                print(bitmap[r][c])
                s += 1
            else:
                bitmap[r][c] = s % 2 == 0

    count = 0
    for l in bitmap:
        for c in l:
            if c:
                count += 1
    print(len(grid[0]) * len(grid) - count)
    print(count)


def main():
    D = open("input/10.in").read()
    grid = D.splitlines()
    start = D.replace("\n", "").index("S")
    r, c = start // len(grid[0]), start % len(grid[0])
    visited = search(grid, r, c)
    inside(grid, visited)


if __name__ == "__main__":
    main()
