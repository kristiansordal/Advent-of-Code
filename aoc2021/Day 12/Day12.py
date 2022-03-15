import re
def part1(caves):
    uniqueCaves = []
    uniqueCaves = [cave for cave in caves if cave not in uniqueCaves] 
    print(uniqueCaves)

    

def main():
    with open('C:\dev\Advent of Code\Advent of Code 2021\Day 12\inputDay12.txt') as file:
        input = [re.split('[- | \n]', line) for line in file] 
        caves = [(cave[0], cave[1].strip()) for cave in input]


    part1(caves)
if __name__ == '__main__':
    main()