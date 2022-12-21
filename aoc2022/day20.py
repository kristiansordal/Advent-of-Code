import copy
def mix(nums):
    copy = copy.deepcopy(nums)

    for i, n in enumerate(nums):



def main():
    with open('input/day20.in') as f:
        nums = [int(x) for x in f.readlines()]
    print(nums)

if __name__ == '__main__':
    main()