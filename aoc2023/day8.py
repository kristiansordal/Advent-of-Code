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


def search(r, s):
    ans, v = 0, set()

    while s not in v:
        ns = list(g.neighbors(r))
        if d[ans % len(d)] == "L":
            r = ns[0]
        else:
            r = ns[1 % len(ns)]
        v.add(r)
        v.add(r[-1])
        ans += 1
    return ans


p1 = search("AAA", "ZZZ")
start_nodes, p2 = [n for n in nodes if n[-1] == "A"], []
for n in start_nodes:
    p2.append(search(n, "Z"))

print(f"P1: {p1}, P2: {lcm(*p2)}")
