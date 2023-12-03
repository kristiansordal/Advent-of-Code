from collections import defaultdict

with open("input/3.in") as f:
    data = f.read().splitlines()
    chars = "/*=$%&+#-@"
    v = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
    gears = [[False for _ in range(len(data[0]))] for _ in range(len(data))]
    ratio = []
    locations = defaultdict(list)
    dirs = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]

    s = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j].isdigit():
                digits = []

                for k in range(3):
                    if 0 <= j + k and j + k < len(data[0]):
                        if data[i][j + k] == "." or data[i][j + k] in chars:
                            break

                        digits.append(data[i][j + k])

                digits = [int(x) for x in digits]

                for k in range(len(digits)):
                    for di, dj in dirs:
                        if (
                            0 <= i + di
                            and i + di < len(data)
                            and 0 <= j + k + dj
                            and j + k + dj < len(data[0])
                            and data[i + di][j + k + dj] in chars
                            and not v[i][j + k]
                        ):
                            for u in range(len(digits)):
                                v[i][j + u] = True
                            s += sum(
                                d * 10**k for k, d in enumerate(reversed(digits))
                            )
                        if (
                            0 <= i + di
                            and i + di < len(data)
                            and 0 <= j + k + dj
                            and j + k + dj < len(data[0])
                            and data[i + di][j + k + dj] == "*"
                            and not gears[i][j + k]
                        ):
                            for u in range(len(digits)):
                                gears[i][j + u] = True

                            if locations[(i + di, j + k + dj)] != 0:
                                num = sum(
                                    d * 10**k for k, d in enumerate(reversed(digits))
                                )
                                locations[(i + di, j + k + dj)].append(num)
                                ratio.append(locations[(i + di, j + k + dj)] * num)
                            else:
                                locations[(i + di, j + k + dj)].append(
                                    sum(
                                        d * 10**k
                                        for k, d in enumerate(reversed(digits))
                                    )
                                )

    print(s)

    s1 = 0
    for k, v in locations.items():
        if len(v) == 2:
            s1 += v[0] * v[1]
    print(s1)
