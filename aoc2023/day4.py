data = open("input/4.in").read().splitlines()
score = 0
hits, counts, cs, ws = [], [1] * len(data), [], []

for i, l in enumerate(data):
    text, card = l.split(":")[0], l.split(":")[1].split("|")
    ws.append(list(map(int, card[0].split())))
    cs.append(list(map(int, card[1].split())))
    hits.append(sum(1 if x in ws[i] else 0 for x in cs[i]))
    score += 2 ** (hits[i] - 1) if hits[i] > 0 else 0

for i in range(len(cs)):
    for j in range(i + 1, i + 1 + hits[i]):
        counts[j] += counts[i]

print(f"P1: {int(score)}, P2: {sum(counts)}")
