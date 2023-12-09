from functools import reduce

D = open("input/9.in").read().splitlines()
seqs = [[int(x) for x in l.split()] for l in D]
p1, p2 = [], []

for s in seqs:
    dt, d = [s], []

    while sum(dt[-1]) != dt[-1][-1] * len(dt[0]):
        for i in range(len(dt[-1]) - 1):
            d.append(dt[-1][i + 1] - dt[-1][i])

        dt.append(d)
        d = []

    p1.append(sum(x[-1] for x in dt))
    p2.append(reduce(lambda acc, x: x[0] - acc, reversed(dt), 0))

print(f"P1: {sum(p1)}, P2: {sum(p2)}")
