from collections import Counter

D = open("input/2.in").read().splitlines()

twos, threes = 0, 0
for d in D:
    c = Counter(d)
    if 2 in c.values():
        twos += 1
    if 3 in c.values():
        threes += 1
p1 = twos * threes
p2 = ""

for i in range(len(D)):
    for j in range(i + 1, len(D)):
        diff = 0
        for k in range(len(D[i])):
            if D[i][k] != D[j][k]:
                diff += 1
        if diff == 1:
            p2 = "".join([D[i][k] for k in range(len(D[i])) if D[i][k] == D[j][k]])
            break

print(f"P1: {p1}, P2: {p2}")
