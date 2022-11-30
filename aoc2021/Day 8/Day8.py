import re
def part1(instructions, nums, visited):
    acc = 0
    i = 0
    while True:
        if visited[i] == True:
            if instructions[i] == 'nop':
                instructions[i] = 'jmp'
            elif instructions[i] == 'jmp':
                instructions[i] = 'nop'
            print('Accumulator: ', acc)
            i+=1
            continue
        elif instructions[i] == 'acc':
            visited[i] = True
            if nums[i][0] == '+':
                acc += int(nums[i][1:])
            elif nums[i][0] == '-':
                acc -= int(nums[i][1:])
            i += 1
            continue
        
        elif instructions[i] == 'nop':
            visited[i] = True
            i += 1
            continue

        elif instructions[i] == 'jmp':
            visited[i] = True
            if nums[i][0] == '+':
                i += int(nums[i][1:])
            elif nums[i][0] == '-':
                i -= int(nums[i][1:])
            continue
        
def part2(instructions, nums, visited):
    acc = 0
    i = 0
    size = len(instructions)
    while True:
        if visited[i] == True:
            print(instructions[i])
            print('Accumulator: ', acc)
            # break
        if instructions[i] == 'acc':
            visited[i] = True
            if nums[i][0] == '+':
                acc += int(nums[i][1:])
            elif nums[i][0] == '-':
                acc -= int(nums[i][1:])
            i += 1
            continue
        
        elif instructions[i] == 'nop':
            visited[i] = True
            # if nums[i][0] == '+':
            #     if i + int(nums[i][1:])
            i += 1
            continue

        elif instructions[i] == 'jmp':
            visited[i] = True
            if nums[i][0] == '+':
                i += int(nums[i][1:])
            elif nums[i][0] == '-':
                i -= int(nums[i][1:])
            continue       
def main():
    instructions = []
    nums = []
    visited = []
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 8\inputDay8.txt') as file:
        # line = file.read()
        # re.split('[\s|,\n]', line) for line in file
        # # line = input.split(' ')
        # instructions = [line[0]]
        # num = [line[1]]
        # instructions = [line.split(' ') for line in file]
        for line in file:
            instruction, num = line.split(' ')
            instructions.append(instruction)
            nums.append(num.strip())
            visited.append(False)

    # part1(instructions, nums, visited)
    part2(instructions, nums, visited)


if __name__ == '__main__':
    main()