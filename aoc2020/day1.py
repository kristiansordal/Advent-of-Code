def part1(nums):
    num = [[x*y for x in nums if x + y == 2020] for y in nums]
    return max(num)[0]

def part2(nums):
    num = [[[x*y*z for x in nums if x + y + z == 2020] for y in nums] for z in nums]
    return max(max(num))[0]
def main():
    with open('input/day1.in') as file:
        nums = [int(x) for x in file.readlines()]
    print(part1(nums))
    print(part2(nums))

if __name__ == '__main__':
    main()