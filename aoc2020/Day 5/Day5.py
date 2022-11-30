import math
from re import I, U
def part1(seats):
    
    seatID = []
    for seat in seats:
        rowUpper = 127
        rowLower = 0
        colUpper = 7
        colLower = 0 
        for char in seat:
            if char == 'F':
                rowUpper = math.floor((rowUpper + rowLower)/ 2)
            elif char == 'B':
                rowLower = math.ceil((rowUpper + rowLower) / 2)
            elif char == 'L':
                colUpper = math.floor((colUpper + colLower) / 2)
            elif char == 'R':
                colLower = math.ceil((colUpper + colLower) / 2)
           
        seatID.append(rowUpper * 8 + colUpper)
        


    print('Highest seat ID: ', max(seatID))

    return seatID

def part2(seatID):

    seatID.sort() 
    for i, id in enumerate(seatID):
        if i < len(seatID):
            if seatID[i + 1] != id + 1:
                print (seatID[i] + 1) 
        
def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 5\inputDay5.txt') as file:
        seats = file.read().splitlines()

    part1(seats)
    part2(part1(seats))

if __name__ == '__main__':
    main()