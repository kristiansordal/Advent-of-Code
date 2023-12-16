D = [*zip(*[[x for x in l] for l in open("input/3.in").read().splitlines()])]
g = "".join(["1" if l.count("1") > l.count("0") else "0" for l in D])
e = "".join(["0" if l.count("1") > l.count("0") else "1" for l in D])

p1 = int(e, 2) * int(g, 2)
print(int("1") & int("0"))
