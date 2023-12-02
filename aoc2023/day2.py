with open("input/2.in") as f:
    data = f.read().splitlines()
    id_sum = 0
    power_sum = 0

    for l in data:
        text, sets = l.split(":")[0], l.split(":")[1].split(" ")[1:]
        game_id = int(text.split(" ")[1])
        mr, mg, mb = 0, 0, 0
        valid = True

        for i in range(0, len(sets), 2):
            color = sets[i + 1].replace(",", "").replace(";", "")
            if color == "red":
                mr = max(mr, int(sets[i]))
            elif color == "green":
                mg = max(mg, int(sets[i]))
            elif color == "blue":
                mb = max(mb, int(sets[i]))

            if mr > 12 or mg > 13 or mb > 14:
                valid = False

        id_sum += game_id if valid else 0
        power_sum += mr * mb * mg

    print(f"P1: { id_sum}, P2: {power_sum}")
