# type: ignore
from re import sub

D = open("input/19.in").read().split("\n\n")
workflows, items = D[0].split("\n"), [sub(r"([A-z]=)|\{|\}", "", e) for e in D[1].split("\n")]
workflows = {w.split("{")[0]: tuple(w.split("{")[1][:-1].split(",")) for w in workflows}  # }}
d = {"x": 0, "m": 1, "a": 2, "s": 3}
A = []


for i in items[:-1]:
    i = eval(i)
    accepted = False
    key = "in"
    while not accepted:
        if key == "A":
            accepted = True
            A.append(i)
            break
        elif key == "R":
            break

        for w in [w.split(":") for w in workflows[key]]:
            if len(w) == 2:
                expr = eval(f"lambda {w[0][0]} : {w[0]}")
                if expr(i[d[w[0][0]]]):
                    key = w[1]
                    break
            else:
                key = w[0]
                break


def get_range(op, num, lo, hi):
    if op == ">":
        lo = max(lo, num + 1)
    elif op == "<":
        hi = min(hi, num - 1)
    elif op == ">=":
        lo = max(lo, num)
    elif op == "<=":
        hi = min(hi, num)
    return (lo, hi)


def get_ranges(op, var, num, xl, xr, ml, mr, al, ar, sl, sr):
    if var == "x":
        xl, xr = get_range(op, num, xl, xr)
    elif var == "m":
        ml, mr = get_range(op, num, ml, mr)
    elif var == "a":
        al, ar = get_range(op, num, al, ar)
    elif var == "s":
        sl, sr = get_range(op, num, sl, sr)

    return (xl, xr, ml, mr, al, ar, sl, sr)


q = [("in", 1, 4000, 1, 4000, 1, 4000, 1, 4000)]
p2 = 0

while q:
    k, xl, xr, ml, mr, al, ar, sl, sr = q.pop(0)

    if k == "A":
        p2 += (xr - xl + 1) * (mr - ml + 1) * (ar - al + 1) * (sr - sl + 1)
        continue
    if k == "R":
        continue

    for w in [w.split(":") for w in workflows[k]]:
        if len(w) == 2:
            var = w[0][0]
            num = int(w[0][2:])
            op = w[0][1]
            key = w[1]
            q.append((key, *get_ranges(op, var, num, xl, xr, ml, mr, al, ar, sl, sr)))
            xl, xr, ml, mr, al, ar, sl, sr = get_ranges(
                "<=" if op == ">" else ">=", var, num, xl, xr, ml, mr, al, ar, sl, sr
            )
        else:
            q.append((w[0], xl, xr, ml, mr, al, ar, sl, sr))
            break

p1 = sum(sum(e) for e in A)
print(f"P1: {p1}, P2: {p2}")
