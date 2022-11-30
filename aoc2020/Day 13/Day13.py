import copy
import math
def part1(timestamp, buses):
    operatingBus = [int(num) for num in buses if num != 'x']
    times = []
    for bus in operatingBus:
        time = timestamp
        while time >= 0:
            time -= bus
        times.append(abs(time))
    ans = abs(min(times) * operatingBus[times.index(min(times))])

    print(ans)

def part2(buses):
    operatingBus = [int(num) for num in buses if num != 'x']
    offset = [i for i, num in enumerate(buses) if num != 'x']
    timeFound = [False] * len(operatingBus)
    time = 1 
    increment = 108569591    
    # num = math.gcd(operatingBus[0], operatingBus[1])
    #find gcd, aka numbers which do not have common factor and multiply them
    #find x + offset % num for num in buses



    # for i, num in enumerate(operatingBus):
    #     isPrime = True
    #     for i in range(1, num):
    #         if num % i == 0 and i != 1 and i != num:
    #             isPrime = False
    #     if isPrime:
    #         lcm *= num

    # for i, num in enumerate(operatingBus):
    #     isPrime = True




    # while not all(timeFound):
    #     timeFound = [False] * len(operatingBus)
    #     time += increment  
    #     for i, num in enumerate(operatingBus):
    #         if (time + offset[i]) % num == 0: timeFound[i] = True
    #         else: timeFound[i] = False
    # print(time)
    num = increment
    while not all((
    (num + 3) % 41 == 0,
    (num + 7)  % 37 == 0,
    (num + 44) % 409 == 0,
    (num + 61) % 17 == 0,
    )):
        num += 108569591
    print(num - 13)

def main():
    with open('C:\dev\Advent of Code\Advent of Code 2020\Day 13\inputDay13.txt') as file:
        timestamp = int(file.readline().strip())
        buses = file.readline().split(',')
    
    part1(timestamp, buses)
    part2(buses)
if __name__ == '__main__':
    main()