from dataclasses import dataclass

def part1(output):
    uniqueLengths = [2, 3, 4, 7]

    u = 0
    for line in output:
        for num in line:
            if (len(num) in uniqueLengths):
                u += 1

    return u


def part2(output, input):
    total = 0
    for i in range(len(input)):
        digMap = {}

        for dig in input[i]:
            if len(dig) == 2:
                digMap[1] = dig
            if len(dig) == 3:
                digMap[7] = dig
            if len(dig) == 4:
                digMap[4] = dig
            if len(dig) == 7:
                digMap[8] = dig
        
        for dig in input[i]:
            if len(dig) == 6:
                if set(digMap[4]).issubset(set(dig)):
                    digMap[9] = dig
                elif set(digMap[1]).issubset(set(dig)):
                    digMap[0] = dig
                else:
                    digMap[6] = dig
            
        for dig in input[i]:
            if len(dig) == 5:
                if set(dig).issubset(set(digMap[6])):
                    digMap[5] = dig
                elif set(digMap[1]).issubset(set(dig)):
                    digMap[3] = dig
                else:
                    digMap[2] = dig

        num = 0 
        for dig in output[i]:
            for key, value in digMap.items():
                if set(dig) == set(value):
                    num = num * 10 + key

        total += num 
    print(f"Total: {total}")


def main():
    with open('inputDay8.txt') as file:
        data = [line for line in file.read().strip().split('\n')]

    output = [line.split('|')[1].strip().split(' ') for line in data]
    input = [line.split('|')[0].strip().split(' ') for line in data]
    print(part1(output))
    part2(output, input)


if __name__ == '__main__':
    main()
