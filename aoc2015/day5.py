D = open("input/5.in").read().splitlines()

p1 = sum(
    1
    for d in D
    if sum(1 for c in d if c in "aeiou") >= 3
    and any(x in d for x in ["ab", "cd", "pq", "xy"]) == False
    and any(x[0] == x[1] for x in zip(d, d[1:]))
)
p2 = 0
for d in D:
    a, b = False, False
    for i in range(len(d) - 2):
        if d[i] == d[i + 2]:
            b = True
            break

    for i in range(0, len(d), 2):
        for j in range(0, len(d), 2):
            if i == j:
                continue
            if d[i : i + 1] == d[j : j + 1]:
                a = True
                break
    print(a, b)
    if a and b:
        p2 += 1

    # if b:
    #     for i in range(0, len(d) - 2, 2):
    #         c1, c2 = d[i : i + 2]

    #         for j in range(i + 2, len(d) - 2, 2):
    #             if d[j : j + 2] == c1 + c2:
    #                 a = True
    # if a and b:
    #     p2 += 1

print(f"P1: {p1}, P2: {p2}")
