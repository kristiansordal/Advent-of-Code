import networkx as nx
from collections import defaultdict

D = open("input/25.in").read().splitlines()
g = nx.DiGraph()

s, e = D[0].split(": ")[0], D[-1].split(": ")[0]

for d in D:
    n, ns = d.split(": ")
    g.add_weighted_edges_from([(n, x, 1) for x in ns.split()], weight="capacity")
    g.add_weighted_edges_from([(x, n, 1) for x in ns.split()], weight="capacity")


# i really gotta go back and actually implement mincut myself, just dont have time right now smh
def find_min_cut(g):
    for s in g.nodes:
        for t in g.nodes:
            if s != t:
                cut, components = nx.minimum_cut(g, s, t)
                if cut == 3:
                    return len(components[0]) * len(components[1])


p1 = find_min_cut(g)
print(f"P1: {p1}")
