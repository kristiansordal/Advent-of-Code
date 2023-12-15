from collections import OrderedDict
from functools import reduce

D = open("input/15.in").read().strip().split(",")
hash = lambda s: reduce(lambda h, x: ((h + ord(x)) * 17) % 256, s, 0)
boxes = [OrderedDict() for _ in range(256)]

p1 = sum(hash(c) for c in D)
D = [x.strip("-").split("=") for x in D]

for d in D:
    if len(d) != 1:
        boxes[hash(d[0])][d[0]] = int(d[1])
    elif boxes[hash(d[0])].get(d[0]):
        boxes[hash(d[0])].pop(d[0])

p2 = sum(sum((i + 1) * (j + 1) * int(v) for j, (_, v) in enumerate(box.items())) for i, box in enumerate(boxes))

print(f"P1: {p1}, P2: {p2}")
