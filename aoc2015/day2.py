from functools import reduce

with open("input/2.in") as f:
    n = f.readlines()
    s1 = 0
    s2 = 0

    for l in n:
        d = sorted([int(x) for x in l.split("x")])
        xs = [d[0] * d[1], d[0] * d[2], d[1] * d[2]]
        v = reduce(lambda x, y: x * y, d)
        p = d[0] * 2 + d[1] * 2
        s1 += sum(2 * x for x in xs) + min(xs)
        s2 += v + p
    print(s2)
