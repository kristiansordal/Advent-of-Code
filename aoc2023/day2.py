with open("input/2.in") as f:
    data = f.read().splitlines()
    id_sum, power_sum = 0, 0

    for l in data:
        text, sets = l.split(":")[0], l.split(":")[1].split(" ")[1:]
        game_id = int(text.split(" ")[1])
        r, g, b, v = 0, 0, 0, 1

        for i in range(0, len(sets), 2):
            color = sets[i + 1].replace(",", "").replace(";", "")
            if color == "red":
                r = max(r, int(sets[i]))
            elif color == "green":
                g = max(g, int(sets[i]))
            elif color == "blue":
                b = max(b, int(sets[i]))

            if r > 12 or g > 13 or b > 14:
                v = 0

        id_sum += game_id * v
        power_sum += r * b * g

    print(f"P1: { id_sum}, P2: {power_sum}")
