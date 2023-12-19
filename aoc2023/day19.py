from re import sub

D = open("input/19.in").read().split("\n\n")
workflows, items = D[0].split("\n"), [sub(r"([A-z]=)|\{|\}", "", e) for e in D[1].split("\n")]
workflows = {w.split("{")[0]: w.split("{")[1][:-1].split(",") for w in workflows}  # }}
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

p1 = sum(sum(e) for e in A)
print(p1)
