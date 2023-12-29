from collections import defaultdict
from dataclasses import dataclass
import pygame as pg
import numpy as np
from heapq import *
import copy

# size of window
w = 1500
h = 400
screen = pg.display.set_mode((w, h))

RED = (200, 45, 21)
BLACK = (0, 0, 0)

# colors of the graph
gridColors = [
    ((250, 250, 110)),
    ((229, 245, 111)),
    ((209, 240, 114)),
    ((189, 234, 117)),
    ((170, 228, 121)),
    ((152, 222, 124)),
    ((134, 215, 128)),
    ((117, 208, 132)),
    ((100, 201, 135)),
    ((84, 193, 138)),
    ((68, 185, 141)),
    ((52, 178, 142)),
    ((35, 170, 143)),
    ((16, 161, 143)),
    ((0, 153, 143)),
    ((0, 145, 141)),
    ((0, 137, 138)),
    ((0, 128, 135)),
    ((0, 120, 130)),
    ((13, 112, 125)),
    ((23, 104, 119)),
    ((31, 95, 112)),
    ((36, 87, 105)),
    ((40, 80, 97)),
    ((42, 72, 88)),
    ((32, 60, 70)),
]

pg.init()
pg.font.init()
pg.display.set_caption("Dijkstra's pathfinding algorithm")

clock = pg.time.Clock()
FPS = 5000

# blocksize for the grid
blockSize = 9
cornerPos = [[(y, x) for x in range(0, w, blockSize)] for y in range(0, h, blockSize)]


class Node:
    def __init__(self, weight, x, y, path):
        self.weight = weight
        self.x = x
        self.y = y
        self.path = path

    def __lt__(self, other):
        return self.weight < other.weight


@dataclass
class Grid:
    # draws the grid
    def draw_grid(blockSize, initialState):
        for row, x in zip(initialState, range(0, w, blockSize)):
            for col, y in zip(row, range(0, h, blockSize)):
                for k, color in enumerate(gridColors):
                    if col == k:
                        rect = pg.Rect(x, y, blockSize, blockSize)
                        pg.draw.rect(screen, color, rect, blockSize)

    # searches the grid, pass the coordinates as a tuple in (x, y) format
    def dijkstra(map, start, end):
        toSearch = []
        endN = (end[1], end[0])
        startN = Node(0, start[1], start[0], [(start[1], start[0])])
        dist = {(startN.x, startN.y): 0}
        found = {(startN.x, startN.y)}

        print(startN.path)
        Grid.add_neighbours(map, toSearch, startN)

        while not endN in found:
            curr = heappop(toSearch)

            if (curr.x, curr.y) in found:
                continue

            found.add((curr.x, curr.y))
            dist[(curr.x, curr.y)] = curr.weight
            Grid.add_neighbours(map, toSearch, curr)

            rect = pg.Rect(curr.y * blockSize, curr.x * blockSize, blockSize, blockSize)
            pg.draw.rect(screen, RED, rect, blockSize)
            pg.display.update()
            clock.tick_busy_loop(FPS)

        Grid.draw_grid(blockSize, map)
        for x, y in curr.path:
            rect = pg.Rect(y * blockSize, x * blockSize, blockSize, blockSize)
            pg.draw.rect(screen, RED, rect, blockSize)
            pg.display.update()
            pg.time.wait(25)
            clock.tick_busy_loop(FPS)

        pg.time.wait(10000)

    def add_neighbours(map, toSearch, curr):
        dir = {(1, 0), (0, 1), (-1, 0), (0, -1)}

        for d in dir:
            xPos = curr.x + d[0]
            yPos = curr.y + d[1]
            if xPos < len(map[0]) and xPos >= 0 and yPos < len(map) and yPos >= 0:
                if not map[yPos][xPos] > (map[curr.y][curr.x]) + 1:
                    newPath = copy.deepcopy(curr.path)
                    newPath.append((xPos, yPos))
                    heappush(toSearch, Node((curr.weight + 1), xPos, yPos, newPath))

        return toSearch


# --- When running the program, press S to start
def main():
    done = False
    play = False

    # input file goes here
    with open("input/day12.in") as f:
        grid_tile = [[c for c in line.strip()] for line in f]

    for i, _ in enumerate(grid_tile):
        for j, _ in enumerate(grid_tile[0]):
            if grid_tile[i][j] == "S":
                grid_tile[i][j] = 0
            elif grid_tile[i][j] == "E":
                grid_tile[i][j] = 26
            else:
                grid_tile[i][j] = ord(grid_tile[i][j]) - 97

    initialState = np.transpose(np.array(grid_tile))
    while not done:
        for e in pg.event.get():
            if e.type == pg.KEYDOWN and e.key == pg.K_s:
                play = True

            Grid.draw_grid(blockSize, initialState)
            pg.display.update()

            if play == True:
                Grid.dijkstra(initialState, (0, 20), (148, 20))
                pg.display.update()


if __name__ == "__main__":
    main()
