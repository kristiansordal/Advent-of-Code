def part1(forrest):
    counter = 0
    rise = 1
    run = 3
    x = 0
    y = 0
    while True:
        y = y + rise
        if y >= len(forrest):
            break
        x = (x + run) % len(forrest[y])
        if forrest[y][x] == '#':
            counter += 1

    return counter

def part2(forrest, rise, run):
    counter = 0
    x = 0
    y = 0
    while True:
        y = y + rise
        if y >= len(forrest):
            break
        x = (x + run) % len(forrest[y])
        if forrest[y][x] == '#':
            counter += 1

    return counter

def ans(forrest):
    answer = 1
    for i in range(0, 8):
        if i % 2 != 0:
            answer *= part2(forrest, 1, i)
        if i == 0:
            answer *= part2(forrest, 2, 1)

    print('The answer is, ', answer)
def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 3\\testinputDay13.txt') as file:
        forrest = file.read().splitlines()

    part1(forrest)
    ans(forrest)
if __name__ == '__main__':
    main()