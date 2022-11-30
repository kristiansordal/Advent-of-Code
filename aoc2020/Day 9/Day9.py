def part1(nums):
    preamble = 24
    for i, num in enumerate(nums):
        if i > preamble:
            valid = findPair(nums, num, i)
            if valid:
                continue
            elif not valid: 
                print('The number containing the weakness is: ',nums[i])
                return nums[i]

def part2(nums):
    invalidNum = part1(nums)
    subNums = []
    for i, num1 in enumerate(nums):
        sum = num1 
        subNums.clear()
        subNums.append(num1)
        for j, num2 in enumerate(nums):
            if j > i:
                subNums.append(num2)
                sum += num2
                if sum == invalidNum:
                    print('Encryption weakness: ', max(subNums) + min(subNums))
                if sum > invalidNum: break
            
def findPair(nums, num, index):
    preamble = 25
    valid = False
    start = index - preamble 
    end = index 
    for i in range(start,end):
        for j in range(start, end):
            if nums[i]+nums[j] == num:
                valid = True
                return valid

    return valid
    

def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 9\inputDay9.txt') as file:
        nums = [int(line.strip()) for line in file]

    # part1(nums)
    part2(nums)
if __name__ == '__main__':
    main()