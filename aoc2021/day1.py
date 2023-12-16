D = open("input/1.in").read().splitlines()
p1 = sum(1 for i in range(1, len(D)) if int(D[i]) > int(D[i - 1]))
p2 = sum(
    1
    for i in range(0, len(D) - 3)
    if sum(int(D[x]) for x in range(i + 1, i + 4)) > sum(int(D[x]) for x in range(i, i + 3))
)
print(f"P1: {p1}, P2: {p2}")
