def part1(dirs):
    direction = { 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0), 'L': (0, -1)}

    code = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    x = 1
    y = 1
    password = 0

    for line in dirs:
        for i, dir in enumerate(line):
            d = direction.get(dir)
            if y + d[0] <= 2 and y + d[0] >= 0 and x + d[1] <= 2 and x + d[1] >= 0:
                x = d[1] + x
                y = d[0] + y
        password = password * 10 + code[y][x]

    print(password)


def part2(dirs):
    direction = {
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1)
    }

    code = [['0', '0', '1', '0', '0'],
            ['0', '2', '3', '4', '0'],
            ['5', '6', '7', '8', '9'],
            ['0', 'A', 'B', 'C', '0'],
            ['0', '0', 'D', '0', '0']]
    x = 0
    y = 2
    password = ''
    path = 0

    for line in dirs:
        for i, dir in enumerate(line):
            d = direction.get(dir)
            if y + d[0] <= 4 and y + d[0] >= 0 and x + d[1] <= 4 and x + d[1] >= 0:
                if code[y + d[0]][x+d[1]] != '0':
                    x = d[1] + x
                    y = d[0] + y
        password += code[y][x] 

    print(password)


def main():
    with open('day2.in') as file:
        dirs = [line for line in file.read().splitlines()]

    part1(dirs)
    part2(dirs)


if __name__ == '__main__':
    main()
