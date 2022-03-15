def main():
    with open('C:\dev\Advent of Code\Advent of Code 2021\Day 19\inputDay19.txt') as file:
        input = file.read().split('\n\n')
        # scanner = [line.split(',') for line in input if 'scanner' not in line]
        scanners = [[num for num in line.split(',')] for line in input if 'scanner' not in input]

    print(scanners)
if __name__ == '__main__':
    main()