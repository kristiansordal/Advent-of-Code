import re
def main():
    with open ('input/day16.in') as f:
        # inp = [[l.split(' ')[1], l.split('=')[1][0], l.split(',')[1:]] for l in f.readlines()]
        inp = [[re.sub('[a-z0-9=;\s,]', '', l)] for l in f.readlines()]
        # for line in f.readlines():
        #     print(line.split(' ')[1])
        #     print(line.split('=')[1][0])
        #     print(line.split())
    print(inp)
        


if __name__ == '__main__':
    main()