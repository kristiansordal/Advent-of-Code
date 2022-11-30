import copy
from os import kill
def part1(seats):
    changedSeats = copy.deepcopy(seats)
    i = 0
    while [[checkAdjacent(seats, changedSeats, i, j) == True for j, seat in enumerate(col) if seat != '.'] for i, col in enumerate(seats)]:
        if seats != changedSeats:
            seats = copy.deepcopy(changedSeats)
            i += 1
            print(i)
        elif seats == changedSeats:
            seats = copy.deepcopy(changedSeats)
            break

    occupied = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                occupied += 1

    print('There are', occupied, ' occupied seats.')

def part2(seats):
    changedSeats = copy.deepcopy(seats)
    i = 0
    while [[checkAdjacentWithSight(seats, changedSeats, i, j) == True for j, seat in enumerate(col) if seat != '.'] for i, col in enumerate(seats)]:
        if seats != changedSeats:
            seats = copy.deepcopy(changedSeats)
            i += 1
            print(i)
        elif seats == changedSeats:
            seats = copy.deepcopy(changedSeats)
            break

    occupied = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                occupied += 1

    print('There are', occupied, ' occupied seats.')

def checkAdjacent(seats, changedSeats, i, j):
    dir = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]

    col = len(seats) - 1
    row = len(seats[0]) - 1

    if seats[i][j] == 'L' and all(seats[i+k][j+l] != '#' for k, l in dir if (0 <= i + k <= col and 0 <= j + l <= row)):
        changedSeats[i][j] = '#'
    
    elif seats[i][j] == '#':
        neighbor = 0
        for k, l in dir:
            if (0 <= i + k <= col and 0 <= j + l <= row) and seats[i+k][j+l] == '#':
                neighbor += 1 
        if neighbor >= 4:
            changedSeats[i][j] = 'L'


def checkAdjacentWithSight(seats, changedSeats, i, j):
    dir = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]

    col = len(seats) - 1
    row = len(seats[0]) - 1

    if seats[i][j] == 'L' and all(seats[i+k][j+l] != '#' for k, l in dir if (0 <= i + k <= col and 0 <= j + l <= row)):
        changedSeats[i][j] = '#'

    elif seats[i][j] == '#':
        neighbor = 0
        for k, l in dir:
            if (0 <= i + k <= col and 0 <= j + l <= row) and seats[i+k][j+l] == '#':
                neighbor += 1 
        if neighbor >= 4:
            changedSeats[i][j] = 'L'

def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 11\inputDay11.txt') as file:
        
        seats = [[char for char in line.strip()] for line in file]

    part1(seats)
if __name__ == '__main__':
    main()