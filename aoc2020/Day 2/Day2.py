import re

def part1(ruleList, passwordList):

    minList = [] 
    maxList = [] 
    characterList = []
    for rule in ruleList:
        print(re.split('[-, \s]', rule))
        min, max, character = re.split('[-, \s]', rule)
        minList.append(int(min))
        maxList.append(int(max))
        characterList.append(character)

    validPasswords = 0

    for i, password in enumerate(passwordList):
        counter = 0
        for character in password:
            if character == characterList[i]:
                counter += 1 

        if counter >= minList[i] and counter <= maxList[i]:
            validPasswords += 1



    print('There are ', validPasswords, " valid passwords")

def part2(ruleList, passwordList):
            
    minList = [] 
    maxList = [] 
    characterList = []
    for rule in ruleList:
        min, max, character = re.split('[-, \s]', rule)
        minList.append(int(min))
        maxList.append(int(max))
        characterList.append(character)

    counter = 0
    for i, password in enumerate(passwordList):
        if (password[minList[i]-1] == characterList[i]) is not (password[maxList[i]-1] == characterList[i]):
            counter += 1

    print('There are ', counter, " valid passwords")

def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 2\inputDay2-2020.txt') as file:
        ruleList = []
        passwordList = []
        for line in file:
            rules, password = line.split(':') 
            ruleList.append(rules)
            passwordList.append(password.strip())

    # part1(ruleList, passwordList)
    part2(ruleList, passwordList)
        
    


if __name__ == '__main__':
    main()
