from math import floor, ceil, prod

D = open("input/6.in").read().splitlines()
tds = list(zip(map(int, D[0].split()[1:]), map(int, D[1].split()[1:])))
tds.append((int((D[0].replace(" ", "")[5:])), int(D[1].replace(" ", "")[9:])))

res = []
for t, d in tds:
    x = (-t - (t**2 - 4 * d) ** 0.5) / -2
    y = (-t + (t**2 - 4 * d) ** 0.5) / -2
    res.append(ceil(x) - floor(y) - 1)

print(f"P1: {prod(res[:-1])}, P2: {res[-1]}")
