import re
def main():
    with open('input/day2.in') as file:
        # inp = [line.strip().split(':')[0] for line in file.readlines()]
        inp = [(re.sub('\D' '', line.split(' ')[0]),line.strip().split(': ')[1]) for line in file.readlines()]

    print(inp)
if __name__ == '__main__':
    main()