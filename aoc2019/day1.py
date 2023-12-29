D = [int(x) for x in open("input/1.in").read().splitlines()]
p1 = sum(x // 3 - 2 for x in D)
p2 = 0

for x in D:
    while x > 0:
        x = x // 3 - 2
        if x > 0:
            p2 += x
print(f"P1: {p1}, P2: {p2}")
