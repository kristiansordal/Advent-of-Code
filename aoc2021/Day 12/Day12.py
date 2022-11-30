def part1(instructions):
    pos = 0+0j 
    currentDir = 1+0j

    value = [int(instruction[1:]) for instruction in instructions]
    action = [instruction[:1] for instruction in instructions]

    direction = {'N':(0+1j), 'E':(1+0j), 'S':(0-1j), 'W':(-1+0j)}
    rotate = {'R': 1/(0+1j), 'L': 0+1j}

    for value, action in zip(value, action):
        if action in direction:
            pos += direction[action] * value
        elif action in rotate:
            currentDir *= rotate[action]**(value//90)
        elif action == 'F':
            pos += value * (currentDir / abs(currentDir))
    
    manhattanDist = (abs(pos.real) + abs(pos.imag))
    print('Manhattan Distance is: ', manhattanDist)

def part2(instructions):

    pos = 0+10j 
    currentDir = 1+0j

    value = [int(instruction[1:]) for instruction in instructions]
    action = [instruction[:1] for instruction in instructions]

    direction = {'N':(0+1j), 'E':(1+0j), 'S':(0-1j), 'W':(-1+0j)}
    rotate = {'R': 1/(0+1j), 'L': 0+1j}

    for value, action in zip(value, action):
        if action in direction:
            pos += direction[action] * value
        elif action in rotate:
            currentDir *= rotate[action]**(value//90)
        elif action == 'F':
            pos += value * (currentDir / abs(currentDir))
    
    manhattanDist = (abs(pos.real) + abs(pos.imag))
    print('Manhattan Distance is: ', manhattanDist)
def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 12\inputDay12.txt') as file:
        input = [line.strip() for line in file]
    part1(input)

if __name__ == '__main__':
    main()