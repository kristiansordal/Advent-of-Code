data = open("input/2.in").read().splitlines()
id_sum, power_sum = 0, 0

for l in data:
    text, sets = l.split(":")[0], l.split(":")[1].split()
    game_id, v = int(text.split()[1]), 1
    cols = {"r": 0, "g": 0, "b": 0}

    for i in range(0, len(sets), 2):
        c = sets[i + 1].replace(",", "").replace(";", "")[0]
        cols[c] = max(cols[c], int(sets[i]))
        v = 0 if cols["r"] > 12 or cols["g"] > 13 or cols["b"] > 14 else 1

    id_sum += game_id * v
    power_sum += cols["r"] * cols["g"] * cols["b"]

print(f"P1: { id_sum}, P2: {power_sum}")
