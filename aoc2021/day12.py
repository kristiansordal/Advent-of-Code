import re
from itertools import chain
from collections import defaultdict

class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def getNeighbours(self, v):
        return self.graph.get(v) if self.graph.get(v) is not None else []

    def dfs(self, root):
        visited = []
        toSearch = []
        toSearch += self.getNeighbours(root)
        curr = root
        visited.append(curr)

        while not len(toSearch) == 0 and 'end' not in visited:
            curr = toSearch.pop()
            # if not curr.isupper() and not curr in visited:
            if curr.isupper() or not curr in visited:
                visited.append(curr)
                toSearch += self.getNeighbours(curr)
        return visited
            


def part1(caves):
    uniqueCaves = {i for i in list(chain(*caves))}
    g = Graph(uniqueCaves)

    for cave in caves:
        g.addEdge(cave[0], cave[1])

    print(g.dfs('start'))

    # print(g.toString(g.graph))


    

def main():
    with open('day12.in') as file:
        input = [re.split('[- | \n]', line) for line in file] 
        caves = [(cave[0], cave[1].strip()) for cave in input]


    print(part1(caves))
if __name__ == '__main__':
    main()
