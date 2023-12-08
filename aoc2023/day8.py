import networkx as nx
from math import lcm

D = open("input/8.in").read().splitlines()
g, d = nx.DiGraph(), D[0]
nodes = [x.split()[0] for x in D[2:]]
edges = [(x.split()[2].replace("(", "")[:-1], x.split()[3][:-1]) for x in D[2:]]
g.add_nodes_from(nodes)

for i, e in enumerate(edges):
    g.add_edge(nodes[i], e[0])
    g.add_edge(nodes[i], e[1])

p1, v, c = 0, set(), "AAA"

while "ZZZ" not in v:
    ns = list(g.neighbors(c))
    if d[p1 % len(d)] == "L":
        c = ns[0]
    else:
        c = ns[1 % len(ns)]
    v.add(c)
    p1 += 1

start_nodes, p2 = [n for n in nodes if n[-1] == "A"], []
for n in start_nodes:
    s, c, v = 0, n, set()

    while "Z" not in v:
        ns = list(g.neighbors(c))
        if d[s % len(d)] == "L":
            c = ns[0]
        else:
            c = ns[1 % len(ns)]
        v.add(c[-1])
        s += 1

    p2.append(s)

print(f"P1: {p1}, P2: {lcm(*p2)}")
