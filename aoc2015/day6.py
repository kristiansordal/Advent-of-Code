D = open("input/6.in").read().splitlines()

instr = []
coords = []
grid = [[0 for _ in range(1000)] for _ in range(1000)]

for d in D:
    if len(d.split()) == 4:
        instr.append(d.split()[0])
    else:
        instr.append(d.split()[1])

    coords.append([
        list(map(int, d.split(" through ")[0].split()[1 if len(d.split()) == 4 else 2].split(","))),
        list(map(int, d.split(" through ")[-1].split(","))),
    ])

for i, (x, y) in zip(instr, coords):

    for r in range(x[0], y[0] + 1):
        for c in range(x[1], y[1] + 1):
            if i == "on":
                grid[r][c] += 1
            elif i == "off":
                grid[r][c] = min(grid[r][c] - 1, 0)
            else:
                grid[r][c] += 2
p1 = 0
for r in grid:
    for c in r:
        if c:
            p1 += c

# p1 = sum(sum(r) for r in grid)
print(p1)
