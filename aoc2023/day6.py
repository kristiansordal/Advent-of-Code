D = open("input/6.in").read().splitlines()
tds = list(zip(list(map(int, D[0].split()[1:])), list(map(int, D[1].split()[1:]))))
time, dist = int((D[0].replace(" ", "")[5:])), int(D[1].replace(" ", "")[9:])
tds.append((time, dist))
p1, p2 = 1, 0

for i, (t, d) in enumerate(tds):
    v, j, tc = 0, 0, t
    while v * tc < d:
        v += 1
        tc -= 1
        j += 1
    if i < len(tds) - 1:
        p1 *= (t - 2 * j + 1) if t % 2 == 1 else (t - 2 * j - 1)
    else:
        p2 = (t - 2 * j + 1) if t % 2 == 1 else (t - 2 * j - 1)

print(f"P1: {p1}, P2: {p2}")
