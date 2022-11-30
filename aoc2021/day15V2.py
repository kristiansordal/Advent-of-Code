from heapq import *
from math import *
class Node:
    def __init__(self, weight, x, y):
        self.weight = weight
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return self.weight < other.weight

def part1(map):
    toSearch = []
    start = Node(map[0][0], 0,0)
    end = (len(map) - 1, len(map[0]) - 1)
    dist = {start : 0}
    found = {(start.x, start.y)}

    add_neighbours(map, toSearch, start)

    while not end in found: 
        curr = heappop(toSearch)

        if (curr.x, curr.y) in found:
            continue
        
        found.add((curr.x, curr.y))
        dist[curr] = curr.weight
        add_neighbours(map, toSearch, curr)
    print(dist[curr] - map[0][0])


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
            heappush(toSearch, Node((map[yPos][xPos] + curr.weight), xPos, yPos))
    
    return toSearch
def translate_risk(risk, x, y, tile_width, tile_height):
    x_translation = floor(x / tile_width)
    y_translation = floor(y / tile_height)

    risk_translation = (risk + x_translation + y_translation -1) % 9 + 1

    return risk_translation

def main():


    with open('inputDay15.txt') as f:
        grid_tile = [[int(risk) for risk in line.strip()] for line in f]

    tile_width = len(grid_tile[0])
    full_width = tile_width * 5
    tile_height = len(grid_tile)
    full_height = tile_height* 5

    full_grid = [[] for y in range(full_height)]

    for y in range(full_height):
        for x in range(full_width):
            full_grid[y].append(translate_risk(grid_tile[y%tile_height][x%tile_width], x, y, tile_width, tile_height))
    
    print(part1(grid_tile))
    print(part1(full_grid))



if __name__ == "__main__":
    main()
