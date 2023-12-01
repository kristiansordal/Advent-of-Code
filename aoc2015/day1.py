with open("input/1.in") as f:
    l = f.read().strip()
    x = [1 if x == "(" else -1 for x in l]
    a = 0
    l = [a := a + n for n in x]
    print(sum(x))
    print(l.index(-1) + 1)
