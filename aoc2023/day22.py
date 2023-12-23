from copy import deepcopy

D = open("input/22.in").read().splitlines()
bricks = []
for d in D:
    st, ed = d.split("~")
    sx, sy, sz = [int(x) for x in st.split(",")]
    ex, ey, ez = [int(x) for x in ed.split(",")]

    B = []
    if sx == ex and sy == ey:
        for z in range(sz, ez + 1):
            B.append((sx, sy, z))
    elif sx == ex and sz == ez:
        for y in range(sy, ey + 1):
            B.append((sx, y, sz))
    elif sy == ey and sz == ez:
        for x in range(sx, ex + 1):
            B.append((x, sy, sz))
    bricks.append(B)

occupied = set((x, y, z) for B in bricks for (x, y, z) in B)


def fall(bricks, ignore=-1):
    fell = True
    fallen_bricks = set()
    while fell:
        fell = False
        for i, B in enumerate(bricks):
            if i == ignore:
                continue

            fall = True
            for x, y, z in B:
                if z == 1:
                    fall = False
                if (x, y, z - 1) in occupied and (x, y, z - 1) not in B:
                    fall = False

            if fall:
                fell = True
                fallen_bricks.add(i)
                for x, y, z in B:
                    occupied.discard((x, y, z))
                    occupied.add((x, y, z - 1))
                bricks[i] = [(x, y, z - 1) for x, y, z in B]
    return bricks, fallen_bricks


bricks, fallen_bricks = fall(bricks)
orig_state = deepcopy(bricks)
orig_occupied = deepcopy(occupied)

p1, p2 = 0, 0
for i, b in enumerate(bricks):
    bricks = deepcopy(orig_state)
    occupied = deepcopy(orig_occupied)

    for x, y, z in b:
        occupied.discard((x, y, z))

    _, fallen_bricks = fall(bricks, i)

    if len(fallen_bricks) == 0:
        p1 += 1
    p2 += len(fallen_bricks)
print(f"P1: {p1}, P2: {p2}")
