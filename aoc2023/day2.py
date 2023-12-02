with open("input/2.in") as f:
    data = f.read().splitlines()

    id_sum = 0
    power_sum = 0

    for l in data:
        text, sets = l.split(":")[0], l.split(":")[1].split(" ")[1:]
        game_id = int(text.split(" ")[1])
        r, g, b = [], [], []
        mr, mg, mb = 0, 0, 0
        valid = True

        for i in range(0, len(sets), 2):
            color = sets[i + 1].replace(",", "").replace(";", "")
            if color == "red":
                r.append(int(sets[i]))
            elif color == "green":
                g.append(int(sets[i]))
            elif color == "blue":
                b.append(int(sets[i]))

            if sum(r) > 12 or sum(g) > 13 or sum(b) > 14:
                valid = False

            if sets[i + 1][-1] == ";" or i + 2 == len(sets):
                mr = max(mr, sum(r))
                mg = max(mg, sum(g))
                mb = max(mb, sum(b))
                r, g, b = [], [], []

        id_sum += game_id if valid else 0
        power_sum += mr * mb * mg

    print(id_sum)
    print(power_sum)
