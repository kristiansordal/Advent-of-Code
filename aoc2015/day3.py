from collections import defaultdict

with open("input/3.in") as f:
    n = f.read().strip()
    d = defaultdict(int)
    s1 = [0, 0]
    s2 = [0, 0]
    d[str(s1)] = 1
    d[str(s2)] = 1
    multiple = 0
    v = set()
    v.add(str(s1))
    v.add(str(s2))
    r = True

    for c in n:
        s = s1 if r else s2

        if c == "^":
            s[1] += 1
            d[str(s)] += 1

        elif c == "v":
            s[1] -= 1
            d[str(s)] += 1
        elif c == ">":
            s[0] += 1
            d[str(s)] += 1
        elif c == "<":
            s[0] -= 1
            d[str(s)] += 1

        if r:
            s1 = s
        else:
            s2 = s

        r = not r
        v.add(str(s))
    print(len(v))
