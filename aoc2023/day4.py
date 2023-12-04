data = open("input/4.in").read().splitlines()
score, hits, c = 0, [0] * len(data), [1] * len(data)

for i, l in enumerate(data):
    card = l.split(":")[1].split("|")
    hits[i] = sum(1 if x in card[0].split() else 0 for x in card[1].split())
    score += 2 ** (hits[i] - 1) if hits[i] > 0 else 0

    for j in range(i + 1, i + 1 + hits[i]):
        c[j] += c[i]

print(f"P1: {int(score)}, P2: {sum(c)}")
