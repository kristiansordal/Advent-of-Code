import re
def part1(passports, info):
    validTerms = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    valid = [passport for passport in passports if all(x in passport for x in validTerms)]
    validPassportCount = len(valid) 

    print(validPassportCount)
    return valid

def part2(term, info):
    validTerms = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    hcl = ['0','1','2','3','4','5','6','7','8','9', 'a', 'b', 'c', 'd', 'e', 'f', '#']
    ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    validPassport = []
    validInfo = []
    validCount = 0

    for passport, info in zip(term, info):
        if all(x in passport for x in validTerms):
            validPassport.append(passport)
            validInfo.append(info)
    
    validCount = len(validPassport)
    
    for passport, info in zip(validPassport, validInfo):
        for term, info in zip(passport, info):
            valid = True
            if term == 'byr':
                if not (1920 <= int(info) <= 2002):
                    valid = False
                    break
            elif term == 'iyr':
                if not (2010 <= int(info) <= 2020):
                    valid = False
                    break
            elif term == 'eyr':
                if not (2020 <= int(info) <= 2030):
                    valid = False
                    break
            elif term == 'hgt':
                if 'cm' in info:
                    if not (150 <= int(info[:-2]) <= 193):
                        valid = False
                        break
                elif 'in' in info:
                    if not (59 <= int(info[:-2]) <= 76):
                        valid = False
                        break
            elif term == 'hcl':
                if len(info) != 7:
                    valid = False
                    break
                else:
                    for x in info:
                        if x not in hcl:
                            valid = False
                            break
            elif term == 'ecl':
                if info not in ecl or len(info) != 3:
                    valid = False
                    break
            elif term == 'pid':
                if len(info) != 9:
                    valid = False
                    break
        if not valid:
            validCount -= 1

        print(validCount - 1)
        
def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 4\inputDay4.txt') as file:
        input = file.read().split('\n\n')
        passports = [re.split('[: | \s ]', line) for line in input]
        term = [[info for i, info in enumerate(passport) if i % 2 == 0] for passport in passports if passport != '']
        info = [[info for i, info in enumerate(passport) if i % 2 != 0] for passport in passports]

    part1(term, info)
    part2(term, info)

if __name__ == '__main__':
    main()