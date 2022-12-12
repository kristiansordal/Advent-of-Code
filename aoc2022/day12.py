from heapq import *
from math import *

class Node:
    def __init__(self, weight, x, y):
        self.weight = weight
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return self.weight < other.weight


def dijkstra(map, start, end):
    toSearch = []
    endN = (end[1], end[0])
    startN = Node(0, start[1], start[0])
    dist = {(startN.x, startN.y) : 0}
    found = {(startN.x, startN.y)}

    add_neighbours(map, toSearch, startN)

    while not endN in found: 
        curr = heappop(toSearch)

        if (curr.x, curr.y) in found:
            continue
        
        found.add((curr.x, curr.y))
        dist[(curr.x, curr.y)] = curr.weight
        add_neighbours(map, toSearch, curr)

    a = []
    for d in dist:
        if map[d[1]][d[0]] == 0:
            a.append(dist[d])

    print('Part 1: ', dist[endN])
    print('Part 2:', min(a))


def add_neighbours(map, toSearch, curr):
    dir = {
        (1,0),
        (0,1),
        (-1,0),
        (0,-1)
    }

    for d in dir:
        xPos = curr.x + d[0]
        yPos = curr.y + d[1]
        if xPos < len(map[0]) and xPos >= 0 and yPos < len(map) and yPos >= 0:
            if not map[yPos][xPos] < (map[curr.y][curr.x]) - 1:
                heappush(toSearch, Node((curr.weight + 1), xPos, yPos))
    
    return toSearch

def main():


    with open('input/day12.in') as f:
        grid_tile = [[c for c in line.strip()] for line in f]


    start = []
    end = []
    for i, _ in enumerate(grid_tile):
        for j, _ in enumerate(grid_tile[0]):
            if grid_tile[i][j] == 'S':
                grid_tile[i][j] = 0
                start  = [i, j]
            elif grid_tile[i][j] == 'E':
                grid_tile[i][j] = 26 
                end = [i, j]
            else:
                grid_tile[i][j] = ord(grid_tile[i][j]) - 97


    dijkstra(grid_tile, end, start)

if __name__ == "__main__":
    main()