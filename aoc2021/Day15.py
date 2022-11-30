import heapq
from collections import defaultdict
from math import inf as INFINITY

def dijkstra(grid):
    height, width = len(grid), len(grid[0])
    start = (0,0)
    end = (height - 1, width - 1)

    queue = [(0, start)]

    minDist = defaultdict(lambda:INFINITY, {start: 0})
    visited = set()

    while queue:
        distance, node = heapq.heappop(queue)

        if node == end:
            return distance

        if node in visited:
            continue

        visited.add(node)
        row, col = node

        for neighbor in neighbors4(row, col, height, width):
            if neighbor in visited:
                continue

            nextRow, nextCol = neighbor
            newDistance = distance + grid[nextRow][nextCol]
            
            if newDistance < minDist[neighbor]:
                minDist[neighbor] = newDistance
                heapq.heappush(queue, (newDistance, neighbor))

    return INFINITY
    

def neighbors4(row, col, height, width):
    directions = ((1,0),(-1,0),(0,1),(0,-1))

    for dirRow, dirCol in directions:
        rowIterator, colIterator = (row + dirRow, col + dirCol)
        if 0 <= rowIterator < width and 0 <= colIterator < height:
            yield rowIterator, colIterator
        

def main():
    with open('C:\dev\Advent of Code\Advent of Code 2021\Day 15\inputDay15.txt') as file:
        input = map(str.rstrip, file) 
        riskMap = list(list(map(int, row)) for row in input)

    print(dijkstra(riskMap))

if __name__ == '__main__':
    main()