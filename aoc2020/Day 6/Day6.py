import re

def part1(groups):
    ans = sum([ansPerGroup(group) for group in groups])
    print(ans)

def part2(groups):
    ans = 1 + sum([allPeopleAns(group) for group in groups])
    print(ans)

def ansPerGroup(group):
    uniqueChar = []
    ans = 0
    for char in group:
        isUnique = True
        for unique in uniqueChar:
            if char == unique:
                isUnique = False
                break

        if isUnique:
            uniqueChar.append(char)
            ans += 1

    return ans

def allPeopleAns(group):
    ans = 0
    size = 1

    for char in group:
        if char == ' ':
            size += 1

    uniqueChar = getUnique(group)

    sumChar = [0] * len(uniqueChar)
    for char in group:
        for i, unique in enumerate(uniqueChar):
            if char == unique:
                sumChar[i] += 1

    ans = 0
    for num in sumChar:
        if num == size:
            ans += 1

    return ans

def getUnique(group):

    uniqueChar = []
    for char in group:
        isUnique = True
        for unique in uniqueChar:
            if char == unique:
                isUnique = False
                break

        if isUnique:
            uniqueChar.append(char)

    return uniqueChar
        
def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 6\inputDay6.txt') as file:
        input = file.read()
        group = input.split('\n\n')
        groups = [line.replace('\n', ' ') for line in group]

    part1(groups)
    part2(groups)

if __name__ == '__main__':
    main()