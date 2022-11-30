def part1(input):
    while len(input) <= 30000000:
        lastNum = input[len(input) - 1]
        spoken = False
        for i, num in enumerate(input):
            if num == lastNum and i != len(input) - 1:
                spoken = True
                break
        if spoken:
            firstOccurence = False
            difference = 0
            for i, num in reversed(list(enumerate(input))):
                if num == lastNum and firstOccurence == False:
                    turn = i
                    firstOccurence = True
                elif num == lastNum and firstOccurence == True:
                    difference = abs(i - turn)
                    break
            input.append(difference)
        else: input.append(0)
    
    print('Number at turn 2020:', lastNum)

def part2(input):
    while len(input) <= 30000000:
    



            

def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 15\inputDay15.txt') as file:

        line = file.read().split(',')
        input = [int(num) for num in line]

    part1(input)
if __name__ == '__main__':
    main()