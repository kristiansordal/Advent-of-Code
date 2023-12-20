# type: ignore
import networkx as nx

D = open("input/20.in").read().splitlines()
g = nx.DiGraph()

for d in D:
    parts = d.split(" -> ")
    vertex_info, neighbors = parts[0], parts[1].split(", ")
    module = ""

    if not vertex_info[0].isalpha():
        module, vertex = vertex_info[0], vertex_info[1:]
    else:
        vertex = vertex_info

    g.add_node(vertex, module=module, state=[False])
    g.add_edges_from([(vertex, neighbor) for neighbor in neighbors])

for n in g.nodes:
    if g.out_degree(n) > 0 and g.nodes[n]["module"] == "&":
        g.nodes[n]["state"] = {ni: False for ni in g.predecessors(n)}


def search(g, root):
    low, high = 0, 0
    for _ in range(1000):
        low += 1
        q = [root]

        while q:
            v = q.pop(0)

            for u in g.neighbors(v):
                pulse = False

                if g.nodes[v]["module"] == "&":
                    pulse = not all(g.nodes[v]["state"].values())
                else:
                    pulse = all(g.nodes[v]["state"])

                if not pulse and u == "rx":
                    print("Hello")

                if pulse:
                    high += 1
                else:
                    low += 1

                if g.nodes[u] != {}:
                    if g.nodes[u]["module"] == "%":
                        if not pulse:
                            g.nodes[u]["state"] = [not g.nodes[u]["state"][0]]
                            q.append(u)

                    else:
                        g.nodes[u]["state"][v] = pulse
                        q.append(u)
    return low, high


low, high = search(g, "broadcaster")
print(low * high)
